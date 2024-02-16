from django.db import models


class ExportConfiguration(models.Model):
    name = models.CharField(max_length=255)
    format = models.CharField(max_length=255)
    dataset = models.CharField(max_length=255)
    table = models.CharField(max_length=255)
    query = models.TextField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    destination_paths = models.TextField(null=True)
