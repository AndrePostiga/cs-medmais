from django.apps import AppConfig
from medmais import container

import views

class PresentationConfig(AppConfig):
    name = 'presentation'

    def ready(self):
        container.wire(packages=[views])