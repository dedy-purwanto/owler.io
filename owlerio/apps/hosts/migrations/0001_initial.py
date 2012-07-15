# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Host'
        db.create_table('hosts_host', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('slug', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal('hosts', ['Host'])

        # Adding model 'UserHost'
        db.create_table('hosts_userhost', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('host', self.gf('django.db.models.fields.related.ForeignKey')(related_name='users', to=orm['hosts.Host'])),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(related_name='user_host', to=orm['auth.User'])),
            ('repo_username', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('repo_userid', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('access_token', self.gf('django.db.models.fields.TextField')()),
            ('access_token_secret', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('preference', self.gf('django.db.models.fields.related.OneToOneField')(related_name='user_host', unique=True, to=orm['preferences.Preference'])),
        ))
        db.send_create_signal('hosts', ['UserHost'])

        # Adding model 'UserRepo'
        db.create_table('hosts_userrepo', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user_host', self.gf('django.db.models.fields.related.ForeignKey')(related_name='repos', to=orm['hosts.UserHost'])),
            ('repo_id', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('repo_owner_username', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('is_valid', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('can_use_title', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('alias', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('preference', self.gf('django.db.models.fields.related.OneToOneField')(related_name='repo', unique=True, to=orm['preferences.Preference'])),
        ))
        db.send_create_signal('hosts', ['UserRepo'])


    def backwards(self, orm):
        # Deleting model 'Host'
        db.delete_table('hosts_host')

        # Deleting model 'UserHost'
        db.delete_table('hosts_userhost')

        # Deleting model 'UserRepo'
        db.delete_table('hosts_userrepo')


    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        'auth.permission': {
            'Meta': {'ordering': "('content_type__app_label', 'content_type__model', 'codename')", 'unique_together': "(('content_type', 'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'hosts.host': {
            'Meta': {'object_name': 'Host'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'slug': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'hosts.userhost': {
            'Meta': {'object_name': 'UserHost'},
            'access_token': ('django.db.models.fields.TextField', [], {}),
            'access_token_secret': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'host': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'users'", 'to': "orm['hosts.Host']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'preference': ('django.db.models.fields.related.OneToOneField', [], {'related_name': "'user_host'", 'unique': 'True', 'to': "orm['preferences.Preference']"}),
            'repo_userid': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'repo_username': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'user_host'", 'to': "orm['auth.User']"})
        },
        'hosts.userrepo': {
            'Meta': {'ordering': "['title', 'alias']", 'object_name': 'UserRepo'},
            'alias': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'can_use_title': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_valid': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'preference': ('django.db.models.fields.related.OneToOneField', [], {'related_name': "'repo'", 'unique': 'True', 'to': "orm['preferences.Preference']"}),
            'repo_id': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'repo_owner_username': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'user_host': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'repos'", 'to': "orm['hosts.UserHost']"})
        },
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

    complete_apps = ['hosts']