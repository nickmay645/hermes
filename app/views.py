from django.shortcuts import render, get_object_or_404, redirect

from django.core.paginator import Paginator
# Create a simple hello world view
from django.http import HttpResponse
from django.views import View

from django.shortcuts import render

from .models import ExportConfiguration
from .forms import ExportConfigurationForm

def index(request):
    return render(request, 'app/base.html')

def home(request):
    return render(request, 'app/home.html')

from django.shortcuts import render
from .models import ExportConfiguration

def export_configurations(request):
    export_configurations_list = ExportConfiguration.objects.all()
    paginator = Paginator(export_configurations_list, 10)  
    page_number = request.GET.get('page')
    export_configurations = paginator.get_page(page_number)

    return render(request, 'app/export_configurations.html', {'export_configurations': export_configurations})

def edit_export_configuration(request, id):
    export_configuration = get_object_or_404(ExportConfiguration, id=id)
    if request.method == 'POST':
        form = ExportConfigurationForm(request.POST, instance=export_configuration)
        if form.is_valid():
            form.save()
            return redirect('export_configurations')
    else:
        form = ExportConfigurationForm(instance=export_configuration)
    return render(request, 'app/edit_export_configuration.html', {'form': form})


def delete_export_configuration(request, id):
    export_configuration = get_object_or_404(ExportConfiguration, id=id)
    if request.method == 'POST':
        export_configuration.delete()
        return redirect('export_configurations')
    return render(request, 'app/delete_export_configuration.html', {'export_configuration': export_configuration})


def create_export_configuration(request):
    if request.method == 'POST':
        form = ExportConfigurationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('export_configurations')
    else:
        form = ExportConfigurationForm()
    return render(request, 'app/create_export_configuration.html', {'form': form})