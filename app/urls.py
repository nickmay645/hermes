
from django.urls import path, include

from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('home/', home, name='home'),
    path('export-configurations/', export_configurations, name='export_configurations'),
    path('edit_export_configuration/<int:id>/',edit_export_configuration, name='edit_export_configuration'),
    path('delete_export_configuration/<int:id>/', delete_export_configuration, name='delete_export_configuration'),
    path('create_export_configuration/', create_export_configuration, name='create_export_configuration'),
    path("accounts/", include("django.contrib.auth.urls")),
]