from django.contrib import admin
from django.utils.translation import ugettext as _
from mptt.admin import MPTTModelAdmin
from .models import Team, Person, Membership, PersonImage

from easy_thumbnails.exceptions import InvalidImageFormatError
from adminsortable.admin import SortableInlineAdminMixin

class PreviewMixin(object):

    def render_preview(self, o):
        if not o.image:
            return u''

        try:
            url = o.image['preview'].url
        except InvalidImageFormatError:
            return u''

        if url:
            return u'<img src="%s">' % url
        else:
            return u''

    render_preview.allow_tags = True
    render_preview.short_description = _(u'Preview')

class PersonImageInline(SortableInlineAdminMixin, admin.TabularInline):
    fields = ('render_preview', 'image', 'title', 'alt', 'ordering', )
    readonly_fields = ('render_preview', )
    model = PersonImage
    extra = 0
    sortable_field_name = 'ordering'

    def render_preview(self, person_image):
        url = person_image.image['preview'].url
        if url:
            return u'<img src="%s">' % url
        else:
            return u''

    render_preview.allow_tags = True
    render_preview.short_description = _(u'Preview')

class MembershipInline(SortableInlineAdminMixin, admin.TabularInline):
    model = Membership
    extra = 0

class PersonAdmin(PreviewMixin, admin.ModelAdmin):
    search_fields = ('first_name', 'last_name', 'position', )
    list_display = ('render_preview', 'first_name', 'last_name', 'position', 'active')
    list_display_links = ('render_preview', 'first_name', 'last_name', )
    fields = (
        ('active', ),
        ('first_name', 'last_name', ),
        ('alias', 'gender', ),
        ('position', 'image', ),
        ('hobbies', ),
        ('abstract', ),
        ('phone', 'email', ),
    )
    inlines = [MembershipInline, PersonImageInline]

class TeamAdmin(PreviewMixin, MPTTModelAdmin):
    list_display = ('is_active', 'render_preview', 'name', )
    list_display_links = ('render_preview', 'name', )
    readonly_fields = ('render_preview', )
    inlines = [MembershipInline]
    fields = (
        ('is_active', ),
        ('name', 'parent', ),
        ('image', ),
        ('description', ),
    )

admin.site.register(Team, TeamAdmin)
admin.site.register(Person, PersonAdmin)
