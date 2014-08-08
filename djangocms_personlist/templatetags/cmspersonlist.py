# -*- coding: utf-8 -*-
from django import template
from django.utils.safestring import mark_safe
from djangocms_personlist.resolvers import reverse
from djangocms_personlist.cms_app import TeamApp

register = template.Library()


def render_img(img):
    return u'<img src="%(url)s" width="%(width)s" height="%(height)s" ' \
        u'title="%(title)s" alt="%(alt)s">' % img


@register.filter()
def image(value, image_format):
    if not value:
        return u''

    _img =value._get_image(image_format)

    return mark_safe(render_img(_img))


@register.filter()
def image_url(value, image_format):
    if not value:
        return u''

    return value._get_image(image_format)['url']


@register.simple_tag(takes_context=True)
def teamindex_url(context, prefix=None, app_name=None):
    return reverse(context['request'], prefix, app_name, 'team-index')


@register.simple_tag(takes_context=True)
def persondetail_url(context, pk, prefix=None, app_name=None):
    return reverse(context['request'], prefix, app_name, 'person-detail', kwargs={
        'pk': pk})


@register.simple_tag(takes_context=True)
def specificteam_url(context, get, prefix=None, app_name=None):
    return "%s?team=%s" % (reverse(context['request'], prefix, app_name, 'team-index'), get)


@register.simple_tag(takes_context=True)
def page_pagination(context, team=None, page=1, prefix=None, app_name=None):
    if team:
        return "%s?team=%s&page=%s" % (reverse(context['request'], prefix, app_name, 'team-index'), team, page)
    else:
        return "%s?page=%s" % (reverse(context['request'], prefix, app_name, 'team-index'), page)