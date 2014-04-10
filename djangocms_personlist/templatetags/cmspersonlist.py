# -*- coding: utf-8 -*-
from django import template
from django.utils.safestring import mark_safe
from djangocms_news.resolvers import reverse

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