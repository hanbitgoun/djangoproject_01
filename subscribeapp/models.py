from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from projectapp.models import Project


class Subscription(models.Model):
    # CASCADE - 종속
    user = models.ForeignKey(User, on_delete=models.CASCADE,
                             related_name='subscription', null=False)

    project = models.ForeignKey(Project, on_delete=models.CASCADE,
                                related_name='subscription', null=False)

    # project 중복 구독 불가
    class Meta:
        unique_together = ['user', 'project']