from .views import *

def ind(request):
    obj = django_url.objects.all()
    return {'com':obj}