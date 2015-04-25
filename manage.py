#!/usr/bin/env python
import os
import sys


project_path = lambda *a: os.path.join(os.path.dirname(__file__), *a)

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "UrlShortener.local")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
