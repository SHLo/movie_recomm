from __future__ import unicode_literals

from django.apps import AppConfig
from main.schedule import ScheduleTimer


class MainConfig(AppConfig):
    name = 'main'

    def ready(self):
        super(MainConfig, self).ready()
        ScheduleTimer(10)
