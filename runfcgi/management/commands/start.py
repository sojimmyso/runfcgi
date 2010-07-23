from django.core.management.base import NoArgsCommand

import common

class Command(NoArgsCommand):
    def handle_noargs(self, **options):
        if common.is_running():
            return
        common.start()
