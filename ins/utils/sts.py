# -*- coding:utf-8 -*-

from __future__ import absolute_import

import base64
import hashlib
import hmac
import time
import logging
from functools import reduce
import requests
try:
    from urllib import quote  # Python 2.X
except ImportError:
    from urllib.parse import quote  # Python 3+

from ins.utils.sts_helper import smart_bytes


LOG = logging.getLogger(__name__)


class Sts(object):

    POLICY = r'''{"statement": [{"action": ["name/cos:*"],"effect": "allow","resource":"*"}],"version": "2.0"}'''
    DURATION = 1800

    def __init__(self, config):
        self.policy = config.get('policy') or self.POLICY
        self.duration = config.get('duration_in_seconds') or self.DURATION
        self.secret_id = config.get('secret_id')
        self.secret_key = config.get('secret_key')
        self.proxy = config.get('proxy')

    def get_credential(self):
        try:
            import ssl
        except ImportError:
            LOG.error("error: no ssl support")

        policy = self.policy
        secret_id = self.secret_id
        secret_key = self.secret_key
        duration = self.duration
        real_url = self.__get_url(policy, duration, secret_id, secret_key)
        try:
            response = requests.get(real_url, proxies=self.proxy)
            return response
        except Exception as e:
            LOG.error("error with : {}".format(e))

    def __get_url(self, policy, duration, secret_id, secret_key, name=''):
        method = 'GET'
        path = 'sts.api.qcloud.com/v2/index.php'
        scheme = 'https://'

        params = {'Action': 'GetFederationToken',
                  'codeMode': 'base64',
                  'Nonce': str(int(time.time()) % 1000000),
                  'Region': '',
                  'RequestClient': 'tac-storage-python',
                  'SecretId': secret_id,
                  'Timestamp': str(int(time.time())),
                  'name': name,
                  'policy': policy,
                  'durationSeconds': str(duration)
                  }

        sign = self.__encrypt(method, path, params)
        params['Signature'] = sign
        flat_params_str = Tools.flat_params(params)

        return scheme + path + '?' + flat_params_str

    def __encrypt(self, method, path, key_values):
        source = Tools.flat_params(key_values)
        source = method + path + '?' + source

        sha1_hmac = hmac.new(smart_bytes(self.secret_key),
                             smart_bytes(source),
                             hashlib.sha1).digest()
        sign_base64 = base64.b64encode(sha1_hmac)
        return quote(sign_base64)


class Tools(object):

    @staticmethod
    def _flat_key_values(a):
        return a[0] + '=' + a[1]

    @staticmethod
    def _link_key_values(a, b):
        return a + '&' + b

    @staticmethod
    def flat_params(key_values):
        key_values = sorted(key_values.items(), key=lambda d: d[0])
        return reduce(Tools._link_key_values, map(Tools._flat_key_values, key_values))
