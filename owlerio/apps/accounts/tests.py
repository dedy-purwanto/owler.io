from django.test import TestCase
from django.contrib.auth.models import User


class ProfileTest(TestCase):

    def test_profile_exist_after_create_user(self):
        user = User.objects.create(username="username", password="123")
        self.assertNotEqual(user.profile, None)

    def test_profile_preference_created(self):
        user = User.objects.create(username="username", password="123")

        self.assertNotEqual(user.profile.preference, None)
