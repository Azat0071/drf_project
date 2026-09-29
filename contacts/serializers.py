from rest_framework import serializers
from .models import Contact

class ContactSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=100, allow_blank=True)
    phone = serializers.CharField(max_length=15, allow_blank=True)
    class Meta:
        model = Contact
        fields = '__all__'

    def validate_names(self, value):
        if value.strip() == "":
            raise serializers.ValidationError("заполниите строку")
        return value

    def validate_phone(self, numbers):
        if len(numbers) < 12:
            raise serializers.ValidationError('не верный номер')
        return numbers