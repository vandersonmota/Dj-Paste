from django.forms.models import ModelForm
from djpaste.models import Snippet

class SnippetForm(ModelForm):
    class Meta:
        model = Snippet
        