# -*- coding: utf-8 -*-

LAST_CAMPAIGN = 'redturtle.monkey.last_campaign'

from plone.dexterity.content import Item
from plone.supermodel import model
from zope.interface import implementer
from zope import schema
from redturtle.monkey import _
from z3c.relationfield.schema import RelationList
from plone.app.z3cform.widget import RelatedItemsFieldWidget
from plone.app.vocabularies.catalog import CatalogSource
from z3c.relationfield.schema import RelationChoice
from plone.autoform import directives as form


class ICampaign(model.Schema):
    """ Marker interface and Dexterity Python Schema for Campaign
    """

    campaign_api_key = schema.TextLine(
        title=_(u"Campaign API key"),
        description=_(u"Custom Mailchimp API key for this campaign"),
        required=False
    )

    campaign_from_email = schema.TextLine(
        title=_(u"Campaign FROM email"),
        description=_(u"Custom Mailchimp FROM email for this campaign"),
        required=False
    )

    campaign_from_name = schema.TextLine(
        title=_(u"Campaign FROM name"),
        description=_(u"Custom Mailchimp FROM name for this campaign"),
        required=False
    )

    campaign_items = RelationList(
        title=_(u'label_campaign_items', default=u'Campaign\'s items'),
        default=[],
        value_type=RelationChoice(
            title=_(u'label_campaign_items', default=u'Campaign\'s items'),
            source=CatalogSource(),
        ),
        required=True
    )
    form.widget('campaign_items',
                RelatedItemsFieldWidget,
                source=CatalogSource()
    )


@implementer(ICampaign)
class Campaign(Item):
    """
    """
    @property
    def api_key(self):
        return self.getCampaign_api_key()

    @property
    def from_name(self):
        return self.getCampaign_from_name()

    @property
    def from_email(self):
        return self.getCampaign_from_email()


