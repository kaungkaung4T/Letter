from rest_framework import serializers
from application.models import AppModel


class AppModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = AppModel
        fields = ['user', 'name', 'image']
        