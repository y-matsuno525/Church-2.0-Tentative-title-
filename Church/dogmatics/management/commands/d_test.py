from dogmatics.models import Preprint
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = "test"

    def handle(self, *args, **options):

        preprints = Preprint.objects.all()

        for preprint in preprints:

            print(preprint.title)
            print(preprint.star_count())

