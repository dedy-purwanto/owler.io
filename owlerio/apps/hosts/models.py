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
