# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import easy_thumbnails.fields


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0013_urlconfrevision'),
        ('sites', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Membership',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('ordering', models.PositiveIntegerField(default=0, verbose_name='Sortierung')),
            ],
            options={
                'ordering': ('ordering',),
                'verbose_name': 'Membership',
                'verbose_name_plural': 'Memberships',
            },
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('image', easy_thumbnails.fields.ThumbnailerImageField(max_length=255, upload_to=b'cms_personlist/', null=True, verbose_name='Bild', blank=True)),
                ('image_width', models.PositiveSmallIntegerField(default=0, null=True, verbose_name='Breite des Originalbildes')),
                ('image_height', models.PositiveSmallIntegerField(default=0, null=True, verbose_name='H\xf6he des Originalbildes')),
                ('active', models.BooleanField(default=True, verbose_name='Aktiv')),
                ('title', models.CharField(max_length=20, null=True, verbose_name='Academic Title', blank=True)),
                ('first_name', models.CharField(max_length=30, verbose_name='Vorname')),
                ('middle_name', models.CharField(max_length=50, null=True, verbose_name='Middle name', blank=True)),
                ('last_name', models.CharField(max_length=30, verbose_name='Nachname')),
                ('alias', models.CharField(max_length=30, null=True, verbose_name='Verlinkung', blank=True)),
                ('abstract', models.TextField(null=True, verbose_name='Abstract', blank=True)),
                ('position', models.CharField(max_length=200, null=True, verbose_name='Position', blank=True)),
                ('city', models.CharField(max_length=100, null=True, verbose_name='City', blank=True)),
                ('phone', models.CharField(max_length=30, null=True, verbose_name='Phone', blank=True)),
                ('email', models.EmailField(max_length=254, null=True, verbose_name='Email', blank=True)),
                ('www', models.URLField(null=True, verbose_name='WWW', blank=True)),
                ('gender', models.CharField(default=b'female', max_length=10, verbose_name='Gender', choices=[(b'female', 'Female'), (b'male', 'Male')])),
                ('hobbies', models.TextField(null=True, verbose_name='Hobbies', blank=True)),
                ('quote', models.TextField(null=True, verbose_name='Quote', blank=True)),
                ('sites', models.ManyToManyField(help_text='Person is associated with a certain site.', to='sites.Site', null=True, verbose_name='Site', blank=True)),
            ],
            options={
                'ordering': ('first_name', 'last_name'),
                'verbose_name': 'Person',
                'verbose_name_plural': 'Persons',
            },
        ),
        migrations.CreateModel(
            name='PersonImage',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('image', easy_thumbnails.fields.ThumbnailerImageField(max_length=255, upload_to=b'cms_personlist/', null=True, verbose_name='Bild', blank=True)),
                ('image_width', models.PositiveSmallIntegerField(default=0, null=True, verbose_name='Breite des Originalbildes')),
                ('image_height', models.PositiveSmallIntegerField(default=0, null=True, verbose_name='H\xf6he des Originalbildes')),
                ('title', models.CharField(default=b'', max_length=150, verbose_name='Bild-Title', blank=True)),
                ('alt', models.CharField(default=b'', max_length=150, verbose_name='Alternativer Bild-Text', blank=True)),
                ('ordering', models.PositiveIntegerField(verbose_name='Sortierung')),
                ('person', models.ForeignKey(verbose_name='Person', to='djangocms_personlist.Person')),
            ],
            options={
                'ordering': ['ordering'],
                'verbose_name': 'Person Image',
                'verbose_name_plural': 'Person Images',
            },
        ),
        migrations.CreateModel(
            name='PersonListPluginModel',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='cms.CMSPlugin')),
                ('title', models.CharField(max_length=150, verbose_name='Headline of the team list')),
                ('layout', models.CharField(max_length=20, verbose_name='Layout', choices=[(b'simple_list.html', 'Simple List of Team Members'), (b'one_portrait.html', 'First Person is highlighted (with Image)'), (b'tiles.html', 'Tiles with Portrait Photo of each Member')])),
            ],
            options={
                'verbose_name': 'Person List Plugin',
                'verbose_name_plural': 'Person List Plugins',
            },
            bases=('cms.cmsplugin',),
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('image', easy_thumbnails.fields.ThumbnailerImageField(max_length=255, upload_to=b'cms_personlist/', null=True, verbose_name='Bild', blank=True)),
                ('image_width', models.PositiveSmallIntegerField(default=0, null=True, verbose_name='Breite des Originalbildes')),
                ('image_height', models.PositiveSmallIntegerField(default=0, null=True, verbose_name='H\xf6he des Originalbildes')),
                ('is_active', models.BooleanField(default=False, verbose_name='aktiv')),
                ('name', models.CharField(max_length=30, verbose_name='Team Name')),
                ('description', models.TextField(null=True, verbose_name='Beschreibung', blank=True)),
                ('lft', models.PositiveIntegerField(editable=False, db_index=True)),
                ('rght', models.PositiveIntegerField(editable=False, db_index=True)),
                ('tree_id', models.PositiveIntegerField(editable=False, db_index=True)),
                ('level', models.PositiveIntegerField(editable=False, db_index=True)),
                ('parent', models.ForeignKey(blank=True, to='djangocms_personlist.Team', null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='personlistpluginmodel',
            name='selected_team',
            field=models.ForeignKey(related_name='team_member', verbose_name='Selected Team', to='djangocms_personlist.Team'),
        ),
        migrations.AddField(
            model_name='person',
            name='teams',
            field=models.ManyToManyField(related_name='team_person', verbose_name='Assigned Teams', through='djangocms_personlist.Membership', to='djangocms_personlist.Team'),
        ),
        migrations.AddField(
            model_name='membership',
            name='person',
            field=models.ForeignKey(to='djangocms_personlist.Person'),
        ),
        migrations.AddField(
            model_name='membership',
            name='team',
            field=models.ForeignKey(to='djangocms_personlist.Team'),
        ),
    ]
