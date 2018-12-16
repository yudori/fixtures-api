from django.conf import settings
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page

from rest_framework import status, generics, mixins, filters
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from accounts.v1.serializers import RegistrationSerializer
from fixtures.models import Team, Fixture
from fixtures.v1.serializers import TeamSerializer, FixtureSerializer
from lib.permissions import is_regular_user, is_admin_user, route_permissions


class TeamListView(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    """
    get:
    Return a list of all the existing teams.

    post:
    Create a new team instance.
    """
    queryset = Team.objects.all()
    serializer_class = TeamSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name',)

    @method_decorator(cache_page(settings.DEFAULT_PAGE_CACHE_SECONDS))
    @route_permissions([is_admin_user, is_regular_user])
    def get(self, request, *args, **kwargs):
        """View all teams."""
        return self.list(request, *args, **kwargs)

    @route_permissions([is_admin_user,])
    def post(self, request, *args, **kwargs):
        """Create a new team."""
        return self.create(request, *args, **kwargs)


class TeamDetailView(mixins.RetrieveModelMixin, mixins.UpdateModelMixin,
                     mixins.DestroyModelMixin, generics.GenericAPIView):
    """
    get:
    Return a specific team instance.

    put:
    Update a specific team instance.

    delete:
    Delete a specific team instance.
    """
    queryset = Team.objects.all()
    serializer_class = TeamSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    @method_decorator(cache_page(settings.DEFAULT_PAGE_CACHE_SECONDS))
    @route_permissions([is_admin_user, is_regular_user])
    def get(self, request, *args, **kwargs):
        """View specific team."""
        return self.retrieve(request, *args, **kwargs)

    @route_permissions([is_admin_user,])
    def put(self, request, *args, **kwargs):
        """Update existing team."""
        return self.update(request, *args, **kwargs)

    @route_permissions([is_admin_user,])
    def delete(self, request, *args, **kwargs):
        """Delete existing team."""
        return self.destroy(request, *args, **kwargs)


class FixtureListView(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    """
    get:
    Return a list of all the existing fixtures.

    post:
    Create a new fixture instance.
    """
    queryset = Fixture.objects.all()
    serializer_class = FixtureSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('home_team__name', 'away_team__name', 'venue')

    @route_permissions([is_regular_user, is_admin_user])
    def get(self, request, *args, **kwargs):
        """View all fixtures."""
        return self.list(request, *args, **kwargs)

    @route_permissions([is_admin_user,])
    def post(self, request, *args, **kwargs):
        """Create a new fixture."""
        return self.create(request, *args, **kwargs)


class FixtureDetailView(mixins.RetrieveModelMixin, mixins.UpdateModelMixin,
                        mixins.DestroyModelMixin, generics.GenericAPIView):
    """
    get:
    Return a specific fixture instance.

    put:
    Update a specific fixture instance.

    delete:
    Delete a specific fixture instance.
    """
    queryset = Fixture.objects.all()
    serializer_class = FixtureSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    @route_permissions([is_regular_user,])
    def get(self, request, *args, **kwargs):
        """View specific fixture."""
        return self.retrieve(request, *args, **kwargs)

    @route_permissions([is_admin_user,])
    def put(self, request, *args, **kwargs):
        """Update existing fixture."""
        return self.update(request, *args, **kwargs)

    @route_permissions([is_admin_user,])
    def delete(self, request, *args, **kwargs):
        """Delete existing fixture."""
        return self.destroy(request, *args, **kwargs)
