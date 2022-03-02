from django.apps import AppConfig
from django.conf import settings
from django.utils.translation import ugettext_lazy as _
from django.db.models.signals import post_save


class AuditsConfig(AppConfig):
    name = 'audits'
    verbose_name = _('Audits')

    def ready(self):
        from . import signal_handlers
        if settings.SYSLOG_ENABLE:
            post_save.connect(signals_handler.on_audits_log_create)
