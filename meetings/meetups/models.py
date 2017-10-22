from django.db import models
from django.conf import settings

CATEGORY_CHOICES = (
    ('CAN', 'Can'),
    ('BETTER_ANOTHER_TIME', 'Better another time'),
    ('MAYBE', 'Maybe'),
    ('CANNOT', 'Can not'),
)

PERIOD_CHOICES = (
    ('day', 'Every day'),
    ('week', 'Every week'),
    ('month', 'Every month'),
    ('year', 'Every year'),
)


class Rule(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    start_time = models.TimeField()
    end_time = models.TimeField()

    period = models.CharField(max_length=120, choices=PERIOD_CHOICES)
    category = models.CharField(max_length=120, choices=CATEGORY_CHOICES)
