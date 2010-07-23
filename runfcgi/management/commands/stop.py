from django.core.management.base import NoArgsCommand

import common

class Command(NoArgsCommand):
    def handle_noargs(self, **options):
        common.stop()
