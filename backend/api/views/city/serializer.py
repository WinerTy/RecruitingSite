from rest_framework import serializers
from database.models import City


class CitySerializer(serializers.ModelSerializer):
    city_name = serializers.CharField(source="translated_city_name")

    class Meta:
        model = City
        fields = ["city_name"]
