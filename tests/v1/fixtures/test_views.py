import uuid

from django.urls import reverse
from django.utils import timezone
from rest_framework import status
from rest_framework.test import APITestCase

from fixtures.models import Team, Fixture
from tests.v1.accounts.test_models import UserFactory
from tests.v1.fixtures.test_models import TeamFactory, FixtureFactory


class TeamTests(APITestCase):

    def setUp(self):
        self.user1 = UserFactory.create(email='user@mydomain.com', is_admin=False)
        self.user1.set_password('test')
        self.user1.save()
        self.user2 = UserFactory.create(email='admin@mydomain.com', is_admin=True)
        self.user2.set_password('test')
        self.user2.save()
        self.team1 = TeamFactory.create(name='Chelsea')
        self.team2 = TeamFactory.create(name='Arsenal')

        # get tokens
        url = reverse('accounts:login')
        data = { 'email': self.user1.email, 'password': 'test' }
        response = self.client.post(url, data)
        self.regular_token = response.json().get('token')
    
        data = { 'email': self.user2.email, 'password': 'test' }
        response = self.client.post(url, data)
        self.admin_token = response.json().get('token')

    def test_list_teams(self):
        url = reverse('fixtures:teams')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

        # try again with token authentication
        self.client.credentials(HTTP_AUTHORIZATION='Token {}'.format(self.regular_token))
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_add_team(self):
        url = reverse('fixtures:teams')
        data = { 'name': 'Man utd' }
        self.client.credentials(HTTP_AUTHORIZATION='Token {}'.format(self.regular_token))
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

        # try with admin token
        self.client.credentials(HTTP_AUTHORIZATION='Token {}'.format(self.admin_token))
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Team.objects.last().name, data.get('name'))

    def test_update_team(self):
        url = reverse('fixtures:team_detail', kwargs={'pk': self.team1.id})
        data = { 'name': 'Chelsea FC' }
        self.client.credentials(HTTP_AUTHORIZATION='Token {}'.format(self.admin_token))
        response = self.client.put(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        team = Team.objects.get(id=self.team1.id)
        self.assertEqual(team.name, data.get('name'))
    
    def test_delete_team(self):
        url = reverse('fixtures:team_detail', kwargs={'pk': self.team1.id})
        self.client.credentials(HTTP_AUTHORIZATION='Token {}'.format(self.admin_token))
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_get_team(self):
        url = reverse('fixtures:team_detail', kwargs={'pk': self.team1.id})
        self.client.credentials(HTTP_AUTHORIZATION='Token {}'.format(self.admin_token))
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('name', response.json().keys())

    def test_search_team(self):
        url = reverse('fixtures:teams')
        self.client.credentials(HTTP_AUTHORIZATION='Token {}'.format(self.regular_token))
        response = self.client.get(url + '?search=doesntexist')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.json().get('results')), 0)

        response = self.client.get(url + '?search=Chels')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.json().get('results')), 1)


class FixtureTests(APITestCase):

    def setUp(self):
        self.user1 = UserFactory.create(email='user@mydomain.com', is_admin=False)
        self.user1.set_password('test')
        self.user1.save()
        self.user2 = UserFactory.create(email='admin@mydomain.com', is_admin=True)
        self.user2.set_password('test')
        self.user2.save()
        self.team1 = TeamFactory.create(id=uuid.uuid4(), name='Chelsea')
        self.team2 = TeamFactory.create(id=uuid.uuid4(), name='Arsenal')
        self.fixture = FixtureFactory.create(home_team=self.team1, away_team=self.team2)

        # get tokens
        url = reverse('accounts:login')
        data = { 'email': self.user1.email, 'password': 'test' }
        response = self.client.post(url, data)
        self.regular_token = response.json().get('token')
    
        data = { 'email': self.user2.email, 'password': 'test' }
        response = self.client.post(url, data)
        self.admin_token = response.json().get('token')

    def test_list_fixtures(self):
        url = reverse('fixtures:fixtures')
        response = self.client.get(url)
        self.client.credentials(HTTP_AUTHORIZATION='Token {}'.format(self.regular_token))
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_add_fixture(self):
        url = reverse('fixtures:fixtures')
        data = {
            'home_team': self.team1.id,
            'away_team': self.team2.id,
            'venue': 'Old Trafford',
            'match_date': timezone.now()
        }
        self.client.credentials(HTTP_AUTHORIZATION='Token {}'.format(self.admin_token))
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(str(Fixture.objects.last()), '{} vs {}'.format(self.team1.name, self.team2.name))

    def test_update_fixture(self):
        url = reverse('fixtures:fixture_detail', kwargs={'pk': self.fixture.id})
        data = {
            'home_team': self.team1.id,
            'away_team': self.team2.id,
            'venue': 'Emirates Stadium',
            'match_date': timezone.now()
        }
        self.client.credentials(HTTP_AUTHORIZATION='Token {}'.format(self.admin_token))
        response = self.client.put(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        team = Fixture.objects.get(id=self.fixture.id)
        self.assertEqual(team.venue, data.get('venue'))

    def test_delete_fixture(self):
        url = reverse('fixtures:fixture_detail', kwargs={'pk': self.fixture.id})
        self.client.credentials(HTTP_AUTHORIZATION='Token {}'.format(self.admin_token))
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_get_fixture(self):
        url = reverse('fixtures:fixture_detail', kwargs={'pk': self.fixture.id})
        self.client.credentials(HTTP_AUTHORIZATION='Token {}'.format(self.regular_token))
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('home_team', response.json().keys())
    
    def test_search_fixture(self):
        url = reverse('fixtures:fixtures')
        self.client.credentials(HTTP_AUTHORIZATION='Token {}'.format(self.admin_token))
        response = self.client.get(url + '?search=doesntexist')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.json().get('results')), 0)

        response = self.client.get(url + '?search=Chels')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.json().get('results')), 1)