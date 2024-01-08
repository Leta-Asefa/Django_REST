from rest_framework import serializers
from .models import Phone
class PhoneSerializer(serializers.ModelSerializer):
    class Meta:
        model=Phone
        fields=['brand','model','storage','ram','frontCamera','backCamera','color','price','os','isActive']





