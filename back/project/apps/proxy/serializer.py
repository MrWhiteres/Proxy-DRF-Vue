from rest_framework import serializers

from project.apps.proxy.models import Site


class SiteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Site
        fields = ['id', 'name', 'site', 'created_at', 'traffic', 'transition']
        read_only_fields = ['id', 'created_at', 'traffic', 'transition']
