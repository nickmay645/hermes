from django import forms
from .models import ExportConfiguration

class ExportConfigurationForm(forms.ModelForm):
    template_name = 'app/export_configuration/export_configuration_form.html'

    class Meta:
        model = ExportConfiguration
        fields = ['name', 'format', 'dataset', 'table', 'query', 'destination_paths']
        labels = {
            "name": ("Export Configuration Name"),
        }
        help_texts = {
            "name": ("Used to identify this export configuration."),
        }
        error_messages = {
            "name": {
                "max_length": ("This writer's name is too long."),
            },
        }