import logging

LOG = logging.getLogger(__name__)


def ping(saying='Hold the door!'):
    """Return a callable for ping api. Make sure you have django installed first.

    Args:
        saying: hello world.

    Usage:
        url(r^ping/?$', ping())
    """

    from raven.contrib.django.raven_compat.models import client
    try:
        1 / 0
    except ZeroDivisionError:
        client.captureException()

    LOG.error('Something went wrong! Test Kibana')
    from django.http import HttpResponse
    return lambda request: HttpResponse(saying + "\n")
