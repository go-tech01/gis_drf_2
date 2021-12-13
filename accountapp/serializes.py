from django.contrib.auth.models import User
from rest_framework import serializers

class NewModelSerializer(serializers.Serializer):
    text = serializers.CharField(max_length=255)
    created_at = serializers.DateTimeField()

class UserSerializer(serializers.ModelSerializer):      # form
    class Meta:
        model = User
        fields = ['username', 'password']

    def save(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user