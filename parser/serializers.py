from rest_framework import serializers
from .models import AstanaHubCompany


class AstanaHubCompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = AstanaHubCompany
        fields = "__all__"
