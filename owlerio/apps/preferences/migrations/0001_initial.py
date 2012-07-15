# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Preference'
        db.create_table('preferences_preference', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('track_request', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('track_response', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('email_errors', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('signature', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('signature_text', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
        ))
        db.send_create_signal('preferences', ['Preference'])


    def backwards(self, orm):
        # Deleting model 'Preference'
        db.delete_table('preferences_preference')


    models = {
        'preferences.preference': {
            'Meta': {'object_name': 'Preference'},
            'email_errors': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'signature': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'signature_text': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'track_request': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'track_response': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        }
    }

    complete_apps = ['preferences']