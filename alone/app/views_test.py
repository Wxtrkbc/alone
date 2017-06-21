# from django.db.models import F
# from django.http import HttpResponse
# from django.conf import settings
#
# from redis import Redis
#
# from alone.app.models import Test
#
#
# def test_mysql(request):
#     test, _ = Test.objects.get_or_create(name='test', defaults={'count': 1})
#     test.count = F('count') + 1
#     test.save(update_fields=['count'])
#     test.refresh_from_db()
#     test = Test.objects.get(name='test')
#     return HttpResponse("count:{}".format(test.count) + "\n")
#
#
# def test_redis(request):
#     reids = Redis(**settings.REDIS)
#     counter = reids.incr('counter')
#     return HttpResponse("counter:{}".format(counter) + "\n")
