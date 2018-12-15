import uuid
from django.db import models


class Team(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    name = models.CharField(max_length=255)

    is_active = models.BooleanField(default=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_last_edited = models.DateTimeField(auto_now=True)

    def __str__(self):
        """
        Unicode representation for an Team model.

        :return: string
        """
        return self.name


class Fixture(models.Model):

    STATUS_PENDING = 0
    STATUS_ONGOING = 1
    STATUS_COMPLETED = 2

    MATCH_STATUS = (
        (STATUS_PENDING, 'Pending'),
        (STATUS_ONGOING, 'Ongoing'),
        (STATUS_COMPLETED, 'Completed')
    )

    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    home_team = models.ForeignKey('fixtures.Team', on_delete=models.CASCADE, related_name='home_fixture')
    away_team = models.ForeignKey('fixtures.Team', on_delete=models.CASCADE, related_name='away_fixture')
    venue = models.CharField(max_length=255, blank=True)
    match_date = models.DateTimeField()
    status = models.IntegerField(choices=MATCH_STATUS, default=STATUS_PENDING)

    date_created = models.DateTimeField(auto_now_add=True)
    date_last_edited = models.DateTimeField(auto_now=True)


    def __str__(self):
        """
        Unicode representation for an Fixture model.

        :return: string
        """
        return '{} vs {}'.format(self.home_team, self.away_team)
