# -*- coding: utf-8 -*-

from rest_framework.exceptions import ValidationError


def check_missing_keys(data, keys):
    return [key for key in keys if key not in data]


def check_body_keys(data, keys):
    keys = check_missing_keys(data, keys)
    if not keys:
        return
    raise ValidationError(detail='Missing required field in request body: {}'.format(keys))
