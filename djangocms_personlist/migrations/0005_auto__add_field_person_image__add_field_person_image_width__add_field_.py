# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Person.image'
        db.add_column(u'djangocms_personlist_person', 'image',
                      self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Person.image_width'
        db.add_column(u'djangocms_personlist_person', 'image_width',
                      self.gf('django.db.models.fields.PositiveSmallIntegerField')(default=0, null=True),
                      keep_default=False)

        # Adding field 'Person.image_height'
        db.add_column(u'djangocms_personlist_person', 'image_height',
                      self.gf('django.db.models.fields.PositiveSmallIntegerField')(default=0, null=True),
                      keep_default=False)

        # Adding field 'Team.image'
        db.add_column(u'djangocms_personlist_team', 'image',
                      self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Team.image_width'
        db.add_column(u'djangocms_personlist_team', 'image_width',
                      self.gf('django.db.models.fields.PositiveSmallIntegerField')(default=0, null=True),
                      keep_default=False)

        # Adding field 'Team.image_height'
        db.add_column(u'djangocms_personlist_team', 'image_height',
                      self.gf('django.db.models.fields.PositiveSmallIntegerField')(default=0, null=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Person.image'
        db.delete_column(u'djangocms_personlist_person', 'image')

        # Deleting field 'Person.image_width'
        db.delete_column(u'djangocms_personlist_person', 'image_width')

        # Deleting field 'Person.image_height'
        db.delete_column(u'djangocms_personlist_person', 'image_height')

        # Deleting field 'Team.image'
        db.delete_column(u'djangocms_personlist_team', 'image')

        # Deleting field 'Team.image_width'
        db.delete_column(u'djangocms_personlist_team', 'image_width')

        # Deleting field 'Team.image_height'
        db.delete_column(u'djangocms_personlist_team', 'image_height')


    models = {
        'cms.cmsplugin': {
            'Meta': {'object_name': 'CMSPlugin'},
            'changed_date': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'creation_date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language': ('django.db.models.fields.CharField', [], {'max_length': '15', 'db_index': 'True'}),
            'level': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'lft': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['cms.CMSPlugin']", 'null': 'True', 'blank': 'True'}),
            'placeholder': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['cms.Placeholder']", 'null': 'True'}),
            'plugin_type': ('django.db.models.fields.CharField', [], {'max_length': '50', 'db_index': 'True'}),
            'position': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'rght': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'tree_id': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'})
        },
        'cms.placeholder': {
            'Meta': {'object_name': 'Placeholder'},
            'default_width': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'slot': ('django.db.models.fields.CharField', [], {'max_length': '50', 'db_index': 'True'})
        },
        u'djangocms_personlist.membership': {
            'Meta': {'object_name': 'Membership'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'person': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['djangocms_personlist.Person']"}),
            'team': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['djangocms_personlist.Team']"})
        },
        u'djangocms_personlist.person': {
            'Meta': {'ordering': "('last_name',)", 'object_name': 'Person'},
            'abstract': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'null': 'True', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'image_height': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0', 'null': 'True'}),
            'image_width': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0', 'null': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True', 'blank': 'True'}),
            'position': ('django.db.models.fields.CharField', [], {'max_length': '150', 'null': 'True', 'blank': 'True'}),
            'teams': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'team_person'", 'symmetrical': 'False', 'through': u"orm['djangocms_personlist.Membership']", 'to': u"orm['djangocms_personlist.Team']"}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'})
        },
        u'djangocms_personlist.personlistpluginmodel': {
            'Meta': {'object_name': 'PersonListPluginModel', '_ormbases': ['cms.CMSPlugin']},
            u'cmsplugin_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['cms.CMSPlugin']", 'unique': 'True', 'primary_key': 'True'}),
            'layout': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'selected_team': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'team_member'", 'to': u"orm['djangocms_personlist.Team']"}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '150'})
        },
        u'djangocms_personlist.team': {
            'Meta': {'object_name': 'Team'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'image_height': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0', 'null': 'True'}),
            'image_width': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0', 'null': 'True'}),
            'level': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'lft': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['djangocms_personlist.Team']", 'null': 'True', 'blank': 'True'}),
            'rght': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'tree_id': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'})
        }
    }

    complete_apps = ['djangocms_personlist']