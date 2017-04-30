# -*- coding: utf-8 -*-


def ping(saying='Hold the door!'):
    """Return a callable for ping api. Make sure you have django installed first.

    Args:
        saying: hello world.

    Usage:
        url(r^ping/?$', ping())
    """
    from django.http import HttpResponse
    return lambda request: HttpResponse(saying + "\n")
