import os

from django.core.management.base import BaseCommand


class DebugCommand(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument("--debug", action="store_true")

    def execute(self, *args, **options):
        # Try to enable vscode debugger
        try:
            import ptvsd

            if options.get("debug", False) and os.getpid() != 1 and not ptvsd.is_attached():
                ptvsd.enable_attach(address=("0.0.0.0", 9001), redirect_output=True)
                print("🖥  Remote debugger waiting for attach.")
                ptvsd.wait_for_attach()
        except (ImportError, OSError) as e:
            print("⚠️  Couldn't start remote debugger:", e)

        return super().execute(*args, **options)
