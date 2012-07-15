from django.db import models
from django.contrib.auth.models import User

from preferences.models import Preference


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


class UserRepoManager(models.Manager):

    use_for_related_fields = True

    def validate_user_repos(self, user):
        repos = UserRepo.objects.filter(user_host__user=user)
        for repo in repos:
            dups = UserRepo.objects.filter(title=repo.title).\
                    filter(user_host__user=user).exclude(pk=repo.pk)
            if dups:
                repo.can_use_title = False
                repo.is_valid = False if not repo.alias else True
                repo.save(validating=True)
                for dup in dups:
                    dup.can_use_title = False
                    dup.is_valid = False if not dup.alias else True
                    dup.save(validating=True)
            else:
                repo.can_use_title = True
                repo.is_valid = True
                repo.save(validating=True)


class UserRepo(models.Model):

    user_host = models.ForeignKey(UserHost, related_name='repos')
    repo_id = models.IntegerField(blank=True, null=True)
    repo_owner_username = models.TextField(blank=True, null=True)
    title = models.CharField(max_length=255)
    is_valid = models.BooleanField(default=True)
    can_use_title = models.BooleanField(default=True)
    alias = models.CharField(blank=True, null=True, max_length=255)
    preference = models.OneToOneField(Preference, related_name='repo')
    objects = UserRepoManager()

    def __unicode__(self):
        return '%s - %s - %s - %s' % (self.user_host.user.username, self.user_host.host.slug, self.repo_id, self.title)

    def save(self, *args, **kwargs):
        validating = False
        if 'validating' in kwargs:
            validating = kwargs.pop('validating')

        try:
            preference = self.preference
        except Preference.DoesNotExist:
            self.preference = Preference.objects.create()

        if not validating:
            UserRepo.objects.validate_user_repos(self.user_host.user)

        super(UserRepo, self).save(*args, **kwargs)

    class Meta:
        ordering = ['title', 'alias']
