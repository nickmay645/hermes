from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404, redirect, render

from .forms import ExportConfigurationForm
from .models import ExportConfiguration


def index(request):
    return redirect("export_configurations")


@login_required
def export_configurations(request):
    export_configurations_list = ExportConfiguration.objects.all()
    paginator = Paginator(export_configurations_list, 10)
    page_number = request.GET.get("page")
    export_configurations = paginator.get_page(page_number)

    return render(
        request,
        "app/export_configuration/export_configurations.html",
        {"export_configurations": export_configurations},
    )


@login_required
def edit_export_configuration(request, id):
    export_configuration = get_object_or_404(ExportConfiguration, id=id)
    if request.method == "POST":
        form = ExportConfigurationForm(request.POST, instance=export_configuration)
        if form.is_valid():
            form.save()
            return redirect("export_configurations")
    else:
        form = ExportConfigurationForm(instance=export_configuration)
    return render(
        request,
        "app/export_configuration/edit_export_configuration.html",
        {"form": form},
    )


@login_required
def delete_export_configuration(request, id):
    export_configuration = get_object_or_404(ExportConfiguration, id=id)
    if request.method == "POST":
        export_configuration.delete()
        return redirect("export_configurations")
    return render(
        request,
        "app/export_configuration/delete_export_configuration.html",
        {"export_configuration": export_configuration},
    )


@login_required
def create_export_configuration(request):
    if request.method == "POST":
        form = ExportConfigurationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("export_configurations")
    else:
        form = ExportConfigurationForm()
    return render(
        request,
        "app/export_configuration/create_export_configuration.html",
        {"form": form},
    )


@login_required
def logout_view(request):
    logout(request)
    return redirect("logout_complete")


def logout_complete(request):
    return render(request, "registration/logout_complete.html")
