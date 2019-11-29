from .debugcommand import DebugCommand
from django.contrib.auth.models import User


class Command(DebugCommand):
    help = "Delete all test users"

    def add_arguments(self, parser):
        parser.add_argument("--debug", action="store_true")

    def handle(self, *args, **options):
        User.objects.filter(email__icontains="usertest").delete()
