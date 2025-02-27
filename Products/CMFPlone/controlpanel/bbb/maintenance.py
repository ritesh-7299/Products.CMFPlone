from plone.base.interfaces import IMaintenanceSchema
from plone.base.interfaces import IPloneSiteRoot
from plone.registry.interfaces import IRegistry
from zope.component import adapts
from zope.component import getUtility
from zope.interface import implementer


@implementer(IMaintenanceSchema)
class MaintenanceControlPanelAdapter:

    adapts(IPloneSiteRoot)

    def __init__(self, context):
        self.context = context
        registry = getUtility(IRegistry)
        self.maintenance_settings = registry.forInterface(
            IMaintenanceSchema, prefix="plone")

    def get_days(self):
        return self.maintenance_settings.days

    def set_days(self, value):
        self.maintenance_settings.days = value

    days = property(get_days, set_days)
