from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model

from octofit_tracker.models import Team, Activity, Leaderboard, Workout

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **kwargs):
        User = get_user_model()
        # Clear collections safely
        User.objects.filter(pk__isnull=False).delete()
        Team.objects.filter(pk__isnull=False).delete()
        Activity.objects.filter(pk__isnull=False).delete()
        Leaderboard.objects.filter(pk__isnull=False).delete()
        Workout.objects.filter(pk__isnull=False).delete()

        # Create teams
        marvel = Team.objects.create(name='Marvel')
        dc = Team.objects.create(name='DC')

        # Create users
        ironman = User.objects.create_user(username='ironman', email='ironman@marvel.com', password='pass')
        batman = User.objects.create_user(username='batman', email='batman@dc.com', password='pass')
        wonderwoman = User.objects.create_user(username='wonderwoman', email='wonderwoman@dc.com', password='pass')
        spiderman = User.objects.create_user(username='spiderman', email='spiderman@marvel.com', password='pass')

        # Create activities
        Activity.objects.create(name='Run', user_id=str(ironman.id))
        Activity.objects.create(name='Swim', user_id=str(batman.id))
        Activity.objects.create(name='Bike', user_id=str(wonderwoman.id))
        Activity.objects.create(name='Yoga', user_id=str(spiderman.id))

        # Create leaderboard
        Leaderboard.objects.create(team_id=str(marvel.id), points=100)
        Leaderboard.objects.create(team_id=str(dc.id), points=90)

        # Create workouts
        Workout.objects.create(name='Pushups', difficulty='Easy')
        Workout.objects.create(name='Deadlift', difficulty='Hard')
        Workout.objects.create(name='Squats', difficulty='Medium')

        self.stdout.write(self.style.SUCCESS('octofit_db database populated with test data'))
