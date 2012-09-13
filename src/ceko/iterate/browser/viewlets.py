import plone.app.layout.viewlets.common
from Acquisition import aq_inner
import plone.app.iterate.browser.control
from Products.Archetypes.interfaces import IReferenceable

class ContentViews(plone.app.layout.viewlets.common.ContentViewsViewlet):
    
    def prepareIterateObjectTabs(self, *args, **kwargs):
        tabs = self.prepareObjectTabs(*args, **kwargs)
        
        if IReferenceable.providedBy(self.context):
            iterate_control = plone.app.iterate.browser.control.Control(self.context, self.request)
            if tabs and iterate_control.checkout_allowed():
                for tab in [e for e in tabs if e['id'] == 'edit']:
                    tab['url'] = self.context.absolute_url() + '/@@content-checkout'
         
        return tabs