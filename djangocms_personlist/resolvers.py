from django.core.urlresolvers import resolve, reverse as _reverse
from django.conf import settings


def reverse(request, prefix, app_name, view_name, kwargs={}):
    _namespace = resolve(request.path).namespace
    if not prefix:
        prefix = settings.SITE_PREFIX
    if app_name is not None:
        _namespace = prefix + '-' + app_name
    return _reverse(u':'.join([_namespace, view_name]), kwargs=kwargs)
