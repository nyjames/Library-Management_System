from django.core.management.base import BaseCommand
from django.test.utils import setup_test_environment
from django.core.management import call_command
import os


class Command(BaseCommand):
    help = 'Run Robot Framework tests'

    def handle(self, *args, **kwargs):
        setup_test_environment()

        # Apply migrations
        call_command('migrate', interactive=False)

        # Directory for report output
        output_dir = os.path.join(os.getcwd(), "test-reports")
        os.makedirs(output_dir, exist_ok=True)

        # Run test suite
        print("Starting Robot Framework Tests...")
        os.system(f"robot --outputdir {output_dir} test-scripts/robot-tests/")
