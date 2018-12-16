from django.urls import path

from fixtures.v1 import views as fixture_views


app_name = 'fixtures'

urlpatterns = [
    path('teams/', fixture_views.TeamListView.as_view(), name='teams'),
    path('teams/<uuid:pk>/', fixture_views.TeamDetailView.as_view(), name='team_detail'),
    path('fixtures/', fixture_views.FixtureListView.as_view(), name='fixtures'),
    path('fixtures/<uuid:pk>/', fixture_views.FixtureDetailView.as_view(), name='fixture_detail'),
]
