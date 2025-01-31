from django.core.management import BaseCommand


class Command(BaseCommand):
    help: str = "Automatically create all Russian cities into database"

    def handle(self, *args, **options):
        pass
