from django.test import TestCase
from django.contrib.auth.models import User

from accounts.models import Profile


class ProfileTest(TestCase):

    def test_profile_exist_after_create_user(self):
        # First user (admin, does not have profile)
        user = User.objects.create(username="admin", password="123")
        try:
            self.assertEqual(user.profile, None)
        except Profile.DoesNotExist:
            pass

        user = User.objects.create(username="username", password="123")
        try:
            self.assertNotEqual(user.profile, None)
        except Profile.DoesNotExist:
            pass


    def test_profile_preference_created(self):
        user = User.objects.create(username="username", password="123")
        self.assertNotEqual(user.profile.preference, None)
