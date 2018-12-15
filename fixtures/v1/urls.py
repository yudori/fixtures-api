from django.urls import path

from fixtures.v1 import views as views_v1


urlpatterns = [
    path('teams/', views_v1.TeamListView.as_view(), name='teams'),
    path('teams/<uuid:pk>/', views_v1.TeamDetailView.as_view(), name='team_detail'),
    path('fixtures/', views_v1.FixtureListView.as_view(), name='fixtures'),
    path('fixtures/<uuid:pk>/', views_v1.FixtureDetailView.as_view(), name='fixture_detail'),
]
