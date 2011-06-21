from django.utils.translation import ugettext_lazy as _
from taggit.forms import TagField
from taggit.managers import TaggableManager as BaseTaggableManager
from taggit_autosuggest.widgets import TagAutoSuggest


class TaggableManager(BaseTaggableManager):

    def formfield(self, form_class=TagField, **kwargs):
        defaults = {
            "label": _("Tags"),
            "help_text": _("A comma-separated list of tags."),
            "required": not self.blank,
            "widget": TagAutoSuggest(),
        }
        defaults.update(kwargs)

        return form_class(**defaults)
