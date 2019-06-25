from zope.interface import implementer, Interface
from zope.component import getMultiAdapter, adapts

from redturtle.monkey.interfaces import IMailchimpSlot, IMailchimpSlotRenderer


@implementer(IMailchimpSlot)
class Slot(object):
    adapts(Interface)
    name = u''

    def __init__(self, context):
        self.context = context
        self.request = context.REQUEST

    def render(self, objs=None, **kw):
        result = []
        for obj in objs:
            view = getMultiAdapter((obj, self.request),
                                    IMailchimpSlotRenderer,
                                    name=self.name)
            result.append(view())
        return '\n'.join(result)


@implementer(IMailchimpSlotRenderer)
class SlotRenderer(object):
    template = None

    def __init__(self, context, request):
        self.context = context
        self.request = request

    def __call__(self):
        return self.template()
