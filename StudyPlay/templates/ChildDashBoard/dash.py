from django.core.urlresolvers import reverse
from django.utils.translation import ugettext_lazy as _
from admin_tools.dashboard import modules, Dashboard

class MyDashboard(Dashboard):

    # we want a 3 columns layout
    columns = 3

    def __init__(self, **kwargs):

        # append an app list module for "Applications"
        self.children.append(modules.AppList(
            title=_('Applications'),
            exclude=('django.contrib.*',),
        ))

        # append an app list module for "Administration"
        self.children.append(modules.AppList(
            title=_('Administration'),
            models=('django.contrib.*',),
        ))

        # append a recent actions module
        self.children.append(modules.RecentActions(
            title=_('Recent Actions'),
            limit=5
        ))