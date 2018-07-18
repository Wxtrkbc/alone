# -*- coding: utf-8 -*-

import logging

from ins.utils.response import error_response, json_response
from ins.utils.exception import AloneException

LOG = logging.getLogger(__name__)
ERR_CODE_MAP = {}


class MiddlewareMixin(object):
    def __init__(self, get_response=None):
        self.get_response = get_response
        super(MiddlewareMixin, self).__init__()

    def __call__(self, request):
        response = None
        if hasattr(self, 'process_request'):
            response = self.process_request(request)
        if not response:
            response = self.get_response(request)
        if hasattr(self, 'process_response'):
            response = self.process_response(request, response)
        return response


class AloneExceptionMiddleware(MiddlewareMixin):
    def process_exception(self, request, exception):
        LOG.error("Capture exception. type: {}, info: {}".format(type(exception), exception))
        if type(exception) == AloneException:
            if type(exception.code) == int:
                return error_response(message=exception.message, status=exception.code)
            return json_response(data={
                'message': exception.message,
                'code': exception.code,
            }, status=get_status_code(exception.code))


def get_status_code(err_code):
    return 400 if err_code not in ERR_CODE_MAP else ERR_CODE_MAP[err_code]
