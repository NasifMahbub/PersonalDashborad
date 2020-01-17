from rest_framework import serializers
from .models import CustomUser
from .sqlalchemymodels import SQLUser

class CustomUserSerializer(serializers.Serializer):
    id = serializers.IntegerField() 
    username = serializers.CharField(max_length = 150, required=True)
    email = serializers.EmailField()
    first_name = serializers.CharField(max_length = 60)
    last_name = serializers.CharField(max_length = 60)
    contact_no = serializers.CharField(max_length = 20)
    image = serializers.CharField(max_length = 512)

    def create(self, validated_data):
        return CustomUser.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.email = validated_data.get('email', instance.email)
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.contact_no = validated_data.get('contact_no', instance.contact_no)
        instance.image = validated_data.get('image', instance.image)
        instance.save()
        return instance


class SQLUserSerializer(serializers.Serializer):
    sqluser_id = serializers.IntegerField() 
    user_name = serializers.CharField(max_length = 150, required=True)
    email_address = serializers.EmailField()
    first_name = serializers.CharField(max_length = 60)
    last_name = serializers.CharField(max_length = 60)
    contact_no = serializers.CharField(max_length = 20)
    image_url = serializers.CharField(max_length = 512)

    def create(self, validated_data):
        return SQLUser.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.email_address = validated_data.get('email_address', instance.email_adress)
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.contact_no = validated_data.get('contact_no', instance.contact_no)
        instance.image_url = validated_data.get('image_url', instance.image_url)
        instance.save()
        return instance
        
