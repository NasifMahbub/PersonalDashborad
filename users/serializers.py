from rest_framework import serializers
from .models import CustomUser
from .sqlalchemymodels import SQLUser

class CustomUserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = CustomUser
        fields = ('id','username', 'first_name', 'last_name', 'email', 'contact_no', 'image')

class SQLUserSerializer(serializers.Serializer):
    sqluser_id = serializers.IntegerField() 
    user_name = serializers.CharField(max_length = 150, required=True)
    email_address = serializers.CharField(max_length = 255)
    first_name = serializers.CharField(max_length = 60)
    last_name = serializers.CharField(max_length = 60)
    contact_no = serializers.CharField(max_length = 20)
    image_url = serializers.CharField(max_length = 512)

    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        return SQLUser.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Snippet` instance, given the validated data.
        """
        instance.email_adress = validated_data.get('email_address', instance.email_address)
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.image_url = validated_data.get('image_url', instance.image_url)
        instance.save()
        return instance
        
