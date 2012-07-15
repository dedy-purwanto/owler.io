from django.test import TestCase
from django.contrib.auth.models import User

from hosts.models import Host, UserHost, UserRepo

class RepoTest(TestCase):

    """
    Create 2 repos with same name (and also alias) for a user, 
    revalidate, and the they are all should become invalid.

    if another user has 1 repo with same name as the first user, 
    it'll pass
    """
    def test_duplicate_repo_name_and_alias(self):
        github = Host.objects.create(slug='github')
        bitbucket = Host.objects.create(slug='bitbucket')

        user_a = User.objects.create(username='a', password='123')
        user_b = User.objects.create(username='b', password='123')

        host_a_github = UserHost.objects.create(host=github, 
                user=user_a, repo_username=user_a.username, 
                repo_userid=user_a.pk, access_token='123')
        host_a_bitbucket = UserHost.objects.create(host=bitbucket,
                user=user_a, 
                repo_username=user_a.username, repo_userid=user_a.pk,
                access_token='123')
        host_b = UserHost.objects.create(host=github, user=user_b, 
                repo_username=user_b.username, repo_userid=user_b.pk,
                access_token='123')

        user_a_repo_a1 = UserRepo.objects.create(user_host=host_a_github,
                repo_id=1, title='repo_a')
        user_a_repo_a2 = UserRepo.objects.create(user_host=host_a_bitbucket,
                repo_id=2, title='repo_a')
        user_a_repo_b = UserRepo.objects.create(user_host=host_a_github,
                repo_id=3, title='repo_b')

        user_b_repo_a = UserRepo.objects.create(user_host=host_b,
                repo_id=1, title='repo_a')
        user_b_repo_b = UserRepo.objects.create(user_host=host_b, repo_id=2,
                title='repo_b')

        self.assertEqual(user_a_repo_a1.is_valid, True)
        self.assertEqual(user_a_repo_a2.is_valid, False)
        self.assertEqual(user_a_repo_b.is_valid, True)
        self.assertEqual(user_b_repo_a.is_valid, True)
        self.assertEqual(user_b_repo_b.is_valid, True)

    def test_duplicate_repo_alias(self):
        github = Host.objects.create(slug='github')
        bitbucket = Host.objects.create(slug='bitbucket')

        user_a = User.objects.create(username='a', password='123')
        user_b = User.objects.create(username='b', password='123')

        host_a_github = UserHost.objects.create(host=github, user=user_a, 
                repo_username=user_a.username, repo_userid=user_a.pk,
                access_token='123')
        host_a_bitbucket = UserHost.objects.create(host=bitbucket, user=user_a, 
                repo_username=user_a.username, repo_userid=user_a.pk,
                access_token='123')
        host_b = UserHost.objects.create(host=github, user=user_b, 
                repo_username=user_b.username, repo_userid=user_b.pk,
                access_token='123')

        user_a_repo_a1 = UserRepo.objects.create(user_host=host_a_github,
                repo_id=1, title='repo_1')
        user_a_repo_a2 = UserRepo.objects.create(user_host=host_a_bitbucket,
                repo_id=2, title='repo_2')
        user_a_repo_b = UserRepo.objects.create(user_host=host_a_github,
                repo_id=3, title='repo_3')

        user_b_repo_a = UserRepo.objects.create(user_host=host_b, repo_id=1,
                title='repo_1')
        user_b_repo_b = UserRepo.objects.create(user_host=host_b, repo_id=2,
                title='repo_2')

        self.assertEqual(user_a_repo_a1.is_valid, True)
        self.assertEqual(user_a_repo_a2.is_valid, True)
        self.assertEqual(user_a_repo_b.is_valid, True)
        self.assertEqual(user_b_repo_a.is_valid, True)
        self.assertEqual(user_b_repo_b.is_valid, True)

        user_a_repo_a1.alias = "ra"
        user_a_repo_a1.save()
        user_a_repo_a2.alias = "rb"
        user_a_repo_a2.save()
        user_a_repo_b.alias = "rb"
        user_a_repo_b.save()
        user_b_repo_a.alias = "ra"
        user_b_repo_a.save()
        user_b_repo_b.alias = "rb"
        user_b_repo_b.save()

        self.assertEqual(user_a_repo_a1.is_valid, True)
        self.assertEqual(user_a_repo_a2.is_valid, True)
        self.assertEqual(user_a_repo_b.is_valid, False)
        self.assertEqual(user_b_repo_a.is_valid, True)
        self.assertEqual(user_b_repo_b.is_valid, True)
