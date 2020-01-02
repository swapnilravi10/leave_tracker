from django.apps import AppConfig


class LeaveBalanceConfig(AppConfig):
    name = 'leave_balance'


def ready(self):
    from leaveUpdater import updater
    updater.start()