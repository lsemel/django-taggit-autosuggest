try:
    from south.modelsinspector import add_ignored_fields
    add_ignored_fields(["^taggit_autosuggest\.managers"])
except ImportError:
    pass  # without south this can fail silently
 
