from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = 'Approved'

    def add_arguments(self, parser):
        parser.add_argument('user_id', nargs='+', type=int, help='user ID')

    def handle(self, *args, **kwargs):
        users_ids = kwargs['user_id']

        for user_id in users_ids:
            try:
                user = User.objects.get(pk=user_id)
                user.is_verified()
                self.stdout.write(f'user {user.username} with id {user_id} verified successfully!')
            except user.DoesNotExist:
                self.stdout.write(f'user with id {user_id} does not exist.')