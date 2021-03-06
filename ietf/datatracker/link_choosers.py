from django.utils.html import escape

from ietf.datatracker.models import RFC, InternetDraft, Charter
from ietf.snippets.models import GlossaryItem


class LinkChooser(object):
    link_type = ''
    model = None

    def __getattribute__(self, name):
        if name == 'name':
            return self.model._meta.verbose_name
        return super(LinkChooser, self).__getattribute__(name)


class RichTextLinkHandler(object):
    @staticmethod
    def get_db_attributes(tag):
        return {'id': tag['data-id'],
                'linktype': tag['data-linktype']}

    @classmethod
    def expand_db_attributes(cls, attrs):
        try:
            page = cls.model.objects.get(id=attrs['id'])
            app = cls.model._meta.app_label
            editor_attrs = 'data-linktype="{}" data-id="{}" data-app="{}"'.format(cls.link_type, page.id, app)
            return '<a {} href="{}">'.format(editor_attrs, escape(page.url))
        except RFC.DoesNotExist:
            return '<a>'


class ExternalRichTextLinkHandler(object):
    """Legacy external link chooser

    This will converts old style to new style links as they are encountered
    It is essentially dropping the external attribute
    """
    link_type = 'external'

    @staticmethod
    def get_db_attributes(tag):
        return {}

    @classmethod
    def expand_db_attributes(cls, attrs, for_editor):
        return '<a href="{}">'.format(escape(attrs['href']))


class RFCLinkChooser(LinkChooser):
    link_type = 'rfc'
    model = RFC


class RFCRichTextLinkHandler(RichTextLinkHandler):
    link_type = 'rfc'
    model = RFC


class InternetDraftLinkChooser(LinkChooser):
    link_type = 'internetdraft'
    model = InternetDraft


class InternetDraftRichTextLinkHandler(RichTextLinkHandler):
    link_type = 'internetdraft'
    model = InternetDraft


class CharterLinkChooser(LinkChooser):
    link_type = 'charter'
    model = Charter


class CharterRichTextLinkHandler(RichTextLinkHandler):
    link_type = 'charter'
    model = Charter


class GlossaryItemLinkChooser(LinkChooser):
    link_type = 'glossaryitem'
    model = GlossaryItem


class GlossaryItemRichTextLinkHandler(RichTextLinkHandler):
    link_type = 'glossaryitem'
    model = GlossaryItem
