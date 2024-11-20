from django.core.management.base import BaseCommand
from dogmatics.models import Preprint,FormalPaper

class Command(BaseCommand):
    help = "条件を満たしたpreprintをjournalへ登録する"

    def handle(self, *args, **options):

        criterion = 0 #これよりスターが多いとjournal掲載
        
        preprints = Preprint.objects.all()

        for preprint in preprints:

            if preprint.star_count() > criterion:

                formal_paper = FormalPaper.objects.get_or_create(preprint=preprint)

