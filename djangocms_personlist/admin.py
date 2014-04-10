from django.contrib import admin
from django.utils.translation import ugettext as _
from mptt.admin import MPTTModelAdmin
from .models import Team, Person, Membership

class PreviewMixin(object):

    def render_preview(self, o):
        if not o.image:
            return u''

        url = o.image['preview'].url
        if url:
            return u'<img src="%s">' % url
        else:
            return u''

    render_preview.allow_tags = True
    render_preview.short_description = _(u'Preview')


class MembershipInline(admin.TabularInline):
    model = Membership
    extra = 0

class PersonAdmin(PreviewMixin, admin.ModelAdmin):
    list_display = ('render_preview', 'first_name', 'last_name', 'position', )
    list_display_links = ('render_preview', 'first_name', 'last_name', )
    fields = (
        ('first_name', 'last_name', 'gender', ),
        ('position', 'image', ),
        ('abstract', ),
        ('phone', 'email', ),
    )
    inlines = [MembershipInline]

class TeamAdmin(PreviewMixin, MPTTModelAdmin):
    list_display = ('render_preview', 'name', )
    list_display_links = ('render_preview', 'name', )
    readonly_fields = ('render_preview', )
    inlines = [MembershipInline]
    fields = (
        ('name', 'parent', ),
        ('image', ),
    )

admin.site.register(Team, TeamAdmin)
admin.site.register(Person, PersonAdmin)
