from rest_framework import status, permissions, generics, mixins
from rest_framework.views import APIView
from rest_framework.response import Response

from accounts.v1.serializers import RegistrationSerializer
from fixtures.models import Team, Fixture
from fixtures.v1.serializers import TeamSerializer, FixtureSerializer


class TeamListView(mixins.ListModelMixin,
                   mixins.CreateModelMixin,
                   generics.GenericAPIView):

    queryset = Team.objects.all()
    serializer_class = TeamSerializer

    def get(self, request, *args, **kwargs):
        """View all teams."""
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        """Create a new team."""
        return self.create(request, *args, **kwargs)


class TeamDetailView(mixins.RetrieveModelMixin,
                     mixins.UpdateModelMixin,
                     mixins.DestroyModelMixin,
                     generics.GenericAPIView):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer

    def get(self, request, *args, **kwargs):
        """View specific team."""
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        """Update existing team."""
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        """Delete existing team."""
        return self.destroy(request, *args, **kwargs)



class FixtureListView(mixins.ListModelMixin,
                      mixins.CreateModelMixin,
                      generics.GenericAPIView):

    queryset = Fixture.objects.all()
    serializer_class = FixtureSerializer

    def get(self, request, *args, **kwargs):
        """View all fixtures."""
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        """Create a new fixture."""
        return self.create(request, *args, **kwargs)


class FixtureDetailView(mixins.RetrieveModelMixin,
                        mixins.UpdateModelMixin,
                        mixins.DestroyModelMixin,
                        generics.GenericAPIView):

    queryset = Fixture.objects.all()
    serializer_class = FixtureSerializer

    def get(self, request, *args, **kwargs):
        """View specific fixture."""
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        """Update existing fixture."""
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        """Delete existing fixture."""
        return self.destroy(request, *args, **kwargs)

