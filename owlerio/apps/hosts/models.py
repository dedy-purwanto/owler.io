from django.db import models
from django.db.models import Q
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

from redis import Redis

from preferences.models import Preference, cache_repo_preference


class Host(models.Model):

    slug = models.CharField(max_length=255)

    def __unicode__(self):
        return self.slug

class UserHost(models.Model):

    host = models.ForeignKey(Host, related_name='users')
    user = models.ForeignKey(User, related_name='user_host')
    repo_username = models.CharField(max_length=255)
    repo_userid = models.IntegerField(blank=True, null=True) 
    access_token = models.TextField()
    access_token_secret = models.TextField(blank=True, null=True) # For Oauth 1.0
    preference = models.OneToOneField(Preference, related_name='user_host')

    def save(self, *args, **kwargs):
        try:
            preference = self.preference
        except Preference.DoesNotExist:
            self.preference = Preference.objects.create()

        super(UserHost, self).save(*args, **kwargs)

    def __unicode__(self):
        return '%s - %s' % (self.user.username, self.host.slug)
