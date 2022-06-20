from django.apps import AppConfig
from medmais import container

import repositories

class DomainConfig(AppConfig):
    name = 'domain'

    def ready(self):
        container.wire(packages=[repositories])