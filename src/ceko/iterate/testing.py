from plone.app.testing import PLONE_FIXTURE
from plone.app.testing import PloneSandboxLayer
from plone.app.testing import IntegrationTesting
from plone.app.testing import FunctionalTesting
from plone.app.testing import applyProfile

from zope.configuration import xmlconfig

class CekoIterate(PloneSandboxLayer):

    defaultBases = (PLONE_FIXTURE, )

    def setUpZope(self, app, configurationContext):
        # Load ZCML for this package
        import ceko.iterate
        xmlconfig.file('configure.zcml',
                       ceko.iterate,
                       context=configurationContext)


    def setUpPloneSite(self, portal):
        pass

CEKO_ITERATE_FIXTURE = CekoIterate()
CEKO_ITERATE_INTEGRATION_TESTING = \
    IntegrationTesting(bases=(CEKO_ITERATE_FIXTURE, ),
                       name="CekoIterate:Integration")