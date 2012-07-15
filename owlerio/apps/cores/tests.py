"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase, Client
from django.contrib.auth.models import User
from cores.middlewares import is_url_allowed

class MiddlewareTest(TestCase):
    def test_email_required_middleware(self):
        user_email = User.objects.create(username='user_email', password='123', email='user_email@localhost.com')
        user_no_email = User.objects.create(username='user_no_email', password='123')
        
        urls = (
                ('/accounts/profile/', True),
                ('/accounts/set-email/', False),
                ('/accounts/logout/', False),
                ('/faq/', False),
                ('/help/', False),
                ('/terms/', False),
        )

        c = Client()

        for url in urls:
            uri = url[0]
            email_required = url[1]

            c.login(username=user_email.username, passowrd=user_email.password)
            self.assertEqual(is_url_allowed(user_email, uri), True)

            c.login(username=user_no_email.username, passowrd=user_no_email.password)
            self.assertEqual(is_url_allowed(user_no_email, uri), False if email_required else True)

