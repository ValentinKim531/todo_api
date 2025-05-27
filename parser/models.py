from django.db import models


class AstanaHubCompany(models.Model):
    number = models.CharField(max_length=10, blank=True, default="")
    date_start = models.CharField(max_length=20, blank=True, default="")
    date_end = models.CharField(max_length=20, blank=True, default="")
    bin = models.CharField(max_length=20, blank=True, default="")
    status = models.CharField(max_length=50, blank=True, default="")
    name = models.CharField(max_length=255, blank=True, default="")

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
