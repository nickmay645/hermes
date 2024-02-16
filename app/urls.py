from django.urls import include, path

from .views import *

export_configration_urlpatterns = [
    path("export_configurations/", export_configurations, name="export_configurations"),
    path(
        "edit_export_configuration/<int:id>/",
        edit_export_configuration,
        name="edit_export_configuration",
    ),
    path(
        "delete_export_configuration/<int:id>/",
        delete_export_configuration,
        name="delete_export_configuration",
    ),
    path(
        "create_export_configuration/",
        create_export_configuration,
        name="create_export_configuration",
    ),
]


account_urlpatterns = [
    path("accounts/", include("django.contrib.auth.urls")),
    path("logout/", logout_view, name="logout"),
    path("logout_complete/", logout_complete, name="logout_complete"),
]

urlpatterns = [
    path("", index, name="index"),
    *account_urlpatterns,
    *export_configration_urlpatterns,
]
