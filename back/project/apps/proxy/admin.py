from django.contrib import admin

from project.apps.proxy.models import Site


# Register your models here.
@admin.register(Site)
class SiteAdmin(admin.ModelAdmin):
    list_display = ['name', 'owner', 'site', 'created_at', 'traffic', 'transition']
