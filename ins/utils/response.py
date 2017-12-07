# coding=utf-8


def json_response(data, status=200):
    from django.http import JsonResponse
    return JsonResponse(data=data, status=status, safe=isinstance(data, dict))


def empty_response():
    from django.http import HttpResponse
    return HttpResponse(status=204)


def error_response(message, status=400, code=None):
    from django.http import JsonResponse
    data = {'message': message}
    if code:
        data['code'] = code
    return JsonResponse(data=data, status=status)
