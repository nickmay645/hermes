from django import forms
from .models import ExportConfiguration

class ExportConfigurationForm(forms.ModelForm):
    class Meta:
        model = ExportConfiguration
        fields = ['name', 'format', 'dataset', 'table', 'query', 'destination_paths']