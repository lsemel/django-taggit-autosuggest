This is my fork of https://bitbucket.org/fabian/django-taggit-autosuggest

*** Credits ***
    This project is directly based on those projects:
    * Alex Gaynor
        * https://github.com/alex/django-taggit
    * Ludwik Trammer:
        * http://code.google.com/p/django-tagging-autocomplete/
    * Jeremy Epstein:
        * https://github.com/Jaza/django-taggit-autocomplete
    * Flavio Curella:
        * https://github.com/fcurella/django-taggit-autocomplete
    * Drew Wilson:
        * http://code.drewwilson.com/entry/autosuggest-jquery-plugin

*** Installation ***
   * Add "taggit_autosuggest" to your INSTALLED_APPS in your project settings
   * Run "python manage.py collectstatic" in your django site dir.
   * Add the following line to your project's urls.py file:
         (r'^taggit_autosuggest/', include('taggit_autosuggest.urls')),


*** Settings ***
    TAGGIT_AUTOSUGGEST_STATIC_BASE_URL:
        Instead of collecting and serving the static files directly, you can
        also set this variable to your static base URL somewhere else.
    TAGGIT_AUTOSUGGEST_MAX_SUGGESTIONS (Defaults to 20): 
        The amount of suggestions is limited, you can raise or lower the limit
        of default 20 using this setting.

*** Usage ***
To enable autosuggesting Tags, just let the tagged model use TaggableManager:
    from django.db import models
    from taggit_autosuggest.managers import TaggableManager


    class SomeModel(models.Model):

        tags = TaggableManager()
