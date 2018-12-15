from rest_framework.serializers import ModelSerializer

from fixtures.models import Fixture, Team


class TeamSerializer(ModelSerializer):
    class Meta:
        model = Team
        fields = ('id', 'name', 'is_active', 'date_created')
        read_only_fields = ('id', 'date_created')


class FixtureSerializer(ModelSerializer):
    home_team = TeamSerializer(read_only=True)
    away_team = TeamSerializer(read_only=True)

    class Meta:
        model = Fixture
        fields = ('id', 'home_team', 'away_team', 'venue', 'match_date', 'status', 'date_created')
        read_only_fields = ('id', 'date_created')
