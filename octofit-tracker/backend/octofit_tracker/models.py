from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    email = models.EmailField(unique=True)
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='octofit_users',
        blank=True,
        help_text='The groups this user belongs to.',
        verbose_name='groups',
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='octofit_users_permissions',
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions',
    )

class Team(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, unique=True)

class Activity(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    user_id = models.CharField(max_length=24)

class Leaderboard(models.Model):
    id = models.AutoField(primary_key=True)
    team_id = models.CharField(max_length=24)
    points = models.IntegerField()

class Workout(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    difficulty = models.CharField(max_length=50)
