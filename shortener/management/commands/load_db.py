from django.core.management.base import BaseCommand, CommandError
from shortener.models import Word
from sanitizer import Sanitizer
import logging

class Command(BaseCommand):
    help = 'Loads database from file'

    def add_arguments(self, parser):
        parser.add_argument('file', help='path to file with rows to load')
        parser.add_argument('--debug', action='store_true', default=False,
                            help='print more details')
        parser.add_argument('--limit', type=int, default=0,
                            help='load only first N rows')

    def handle(self, *args, **options):
        if (options['debug']): logging.basicConfig(level=logging.DEBUG)
        count=0
        with open(options['file'], 'r') as file:
            for word in file:
                Word(word=Sanitizer.sanitize(word)).save()
                count+=1
                if (options['limit'] == count): break
        self.stdout.write('Successfully loaded {} words'.format(count))