from rest_framework import serializers
from .models import Recommended

class RecommendedSerializers(serializers.ModelSerializer):
    class Meta:
        model = Recommended()
        fields = 'recommended_name'