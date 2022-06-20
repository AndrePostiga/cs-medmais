from django.apps import AppConfig
from medmais import container

import Services

class ApplicationConfig(AppConfig):
    name = 'application'

    def ready(self):
        container.wire(packages=[Services])
