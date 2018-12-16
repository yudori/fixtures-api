import factory
from django.test import TestCase
from django.utils import timezone

from fixtures.models import Team, Fixture


class TeamFactory(factory.DjangoModelFactory):
    name = 'Default Team'
    is_active = True

    class Meta:
        model = Team


class FixtureFactory(factory.DjangoModelFactory):
    venue = 'Default Venue'
    match_date = timezone.now()
    status = Fixture.STATUS_PENDING

    class Meta:
        model = Fixture


class FixturesModelsTests(TestCase):
    def setUp(self):
        self.team1 = TeamFactory.create(name='Chelsea')
        self.team2 = TeamFactory.create(name='Arsenal')
        self.fixture = FixtureFactory.create(home_team=self.team1, away_team=self.team2)

    def test_unicode(self):
        self.assertEqual(str(self.team1), 'Chelsea')
        self.assertEqual(str(self.team2), 'Arsenal')
        self.assertEqual(str(self.fixture), 'Chelsea vs Arsenal')

