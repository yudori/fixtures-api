import factory
from django.test import TestCase

from accounts.models import User


class UserFactory(factory.DjangoModelFactory):
    first_name = 'John'
    last_name = 'Doe'
    is_active = True

    class Meta:
        model = User
        django_get_or_create = ('email',)


class AccountsModelsTests(TestCase):
    def setUp(self):
        self.user = UserFactory.create(email='test@test.com')

    def test_unicode(self):
        self.assertEqual(str(self.user), 'test@test.com')
