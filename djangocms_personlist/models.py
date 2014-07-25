from cms.models.pluginmodel import CMSPlugin
from django.db import models
from django.utils.translation import ugettext as _
from django.core.urlresolvers import reverse
from easy_thumbnails.fields import ThumbnailerImageField
from easy_thumbnails.files import get_thumbnailer
from easy_thumbnails.exceptions import InvalidImageFormatError
import mptt
import settings

GENDER_CHOICES = (
    ('female', _(u'Female')),
    ('male', _(u'Male')),
)

DJANGOCMS_PERSONLIST_TEMPLATES = (
    ('simple_list.html', _(u'Simple List of Team Members')),
    ('one_portrait.html', _(u'First Person is highlighted (with Image)')),
    ('tiles.html', _(u'Tiles with Portrait Photo of each Member')),
)

if hasattr(settings, 'DJANGOCMS_PERSONLST_TEMPLATES'):
    DJANGOCMS_PERSONLIST_TEMPLATES = settings.DJANGOCMS_PERSONLIST_TEMPLATES


class ImageMixin(models.Model):
    image = ThumbnailerImageField(
        blank=True,
        null=True,
        upload_to='cms_personlist/',
        max_length=255,
        verbose_name=_(u'Image'))

    image_width = models.PositiveSmallIntegerField(
        default=0,
        null=True,
        verbose_name=_(u'Original Image Width'))

    image_height = models.PositiveSmallIntegerField(
        default=0,
        null=True,
        verbose_name=_(u'Original Image Height'))

    def get_image_fallback(self):
        return None

    def _get_image(self, image_format):
        _image_format = settings.THUMBNAIL_ALIASES[''][image_format]
        _img = self.image
        if not _img:
            _img = self.get_image_fallback()
        try:
            img = get_thumbnailer(_img).get_thumbnail(_image_format)
            return {
                'url': img.url,
                'width': img.width,
                'height': img.height,
                'alt': self.get_image_alt(),
                'title': self.get_image_title(),
            }
        except (UnicodeEncodeError, InvalidImageFormatError):
            return None

    def get_image_title(self):
        raise NotImplementedError(
            'A  ImageMixin class requires a .get_image_title method')

    def get_image_alt(self):
        raise NotImplementedError(
            'A  ImageMixin class requires a .get_image_alt method')

    class Meta:
        abstract = True


class Team(ImageMixin, models.Model):
    parent = models.ForeignKey(
        'self',
        blank=True,
        null=True)

    name = models.CharField(
        max_length=30,
        verbose_name=_(u'Team Name'))

    description = models.TextField(
        blank=True,
        null=True,
        verbose_name=_(u'Description')
    )

    def get_image_title(self):
        return self.name

    def get_image_alt(self):
        return self.name

    def __unicode__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('personlist-team', args=[self.pk])

try:
    mptt.register(Team)
except mptt.AlreadyRegistered:
    pass

class PersonListPluginModel(CMSPlugin):
    title = models.CharField(
        max_length=150,
        verbose_name=_(u'Headline of the team list'))
    selected_team = models.ForeignKey(
        Team,
        related_name='team_member',
        verbose_name=_(u'Selected Team'))
    layout = models.CharField(
        max_length=20,
        choices=DJANGOCMS_PERSONLIST_TEMPLATES,
        verbose_name=_(u'Layout'))

    class Meta:
        verbose_name = _(u'Person List Plugin')
        verbose_name_plural = _(u'Person List Plugins')


class Membership(models.Model):
    team = models.ForeignKey(Team)
    person = models.ForeignKey('Person')
    ordering = models.PositiveIntegerField(
        default=0,
        verbose_name=_(u'Ordering'))

    class Meta:
        ordering = ('ordering', )
        verbose_name = _(u'Membership')
        verbose_name = _(u'Memberships')


class Person(ImageMixin, models.Model):
    teams = models.ManyToManyField(
        Team,
        through=Membership,
        related_name='team_person',
        verbose_name=_(u'Assigned Teams'))
    title = models.CharField(
        max_length=20,
        null=True,
        blank=True,
        verbose_name=_(u'Academic Title'))
    first_name = models.CharField(
        max_length=30,
        verbose_name=_(u'First name'))
    middle_name = models.CharField(
        max_length=50,
        null=True,
        blank=True,
        verbose_name=_(u'Middle name'))
    last_name = models.CharField(
        max_length=30,
        verbose_name=_(u'Last name'))
    alias = models.CharField(
        max_length=30,
        null=True,
        blank=True,
        verbose_name=_(u'Alias'))
    abstract = models.TextField(
        null=True,
        blank=True,
        verbose_name=_(u'Abstract'))
    position = models.CharField(
        max_length=200,
        null=True,
        blank=True,
        verbose_name=_(u'Position'))
    city = models.CharField(
        max_length=100,
        null=True,
        blank=True,
        verbose_name=_(u'City'))
    phone = models.CharField(
        max_length=30,
        null=True,
        blank=True,
        verbose_name=_(u'Phone'))
    email = models.EmailField(
        null=True,
        blank=True,
        verbose_name=_(u'Email'))
    www = models.URLField(
        null=True,
        blank=True,
        verbose_name=_(u'WWW'))
    gender = models.CharField(
        max_length=10,
        default='female',
        choices=GENDER_CHOICES,
        verbose_name=_(u'Gender'))
    hobbies = models.TextField(
        null=True,
        blank=True,
        verbose_name=_(u'Hobbies')
    )
    quote = models.TextField(
        null=True,
        blank=True,
        verbose_name=_(u'Quote')
    )

    def get_image_title(self):
        return self.name

    def get_image_alt(self):
        return self.position

    def get_image_fallback(self):
        if self.gender == 'female':
            return u'defaults/female.jpg'
        else:
            return u'defaults/male.jpg'

    @property
    def name(self):
        items = []
        if self.title:
            items.append(self.title)
        items.append(self.first_name)
        items.append(self.last_name)
        return u' '.join(items)

    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ('last_name', )
        verbose_name = _('Person')
        verbose_name_plural = _('Persons')

class PersonImage(ImageMixin, models.Model):

    title = models.CharField(
        blank=True,
        default='',
        max_length=150,
        verbose_name=_(u'Image Title'))

    alt = models.CharField(
        blank=True,
        default='',
        max_length=150,
        verbose_name=_(u'Alternative Image Text'))

    ordering = models.PositiveIntegerField(
        verbose_name=_(u'Ordering'))

    person = models.ForeignKey(Person,
        verbose_name=_(u'Person'))

    def get_title(self):
        if self.title:
            return self.title
        return self.person.title

    def get_alt(self):
        if self.alt:
            return self.alt
        return u'Picture %s' % (self.ordering + 1)

    def __unicode__(self):
        if self.title:
            return self.title
        if self.alt:
            return self.alt
        return _(u'Image #%s') % self.ordering

    class Meta:
        ordering = ['ordering']
        verbose_name = _(u'Person Image')
        verbose_name_plural = _(u'Person Images')

