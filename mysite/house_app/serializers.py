from django.contrib.auth import authenticate

from .models import *
from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken


class UserProfileRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ('username', 'email', 'password', )
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = UserProfile.objects.create_user(**validated_data)
        return user


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        user = authenticate(**data)
        if user and user.is_active:
            return user
        raise serializers.ValidationError("Неверные учетные данные")

    def to_representation(self, instance):
        refresh = RefreshToken.for_user(instance)
        return {
            'user': {
                'username': instance.username,
                'email': instance.email,
            },
            'access': str(refresh.access_token),
            'refresh': str(refresh),
        }





class UserProfileListSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['id','age','username','role','avatar']

class UserProfileDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = [
            'id','password','last_login',
            'is_superuser','username','first_name','last_name','email','is_staff','is_active',
            'date_joined','age','phone_number','avatar','role','groups','user_permissions']

class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = ['city_name']


class PropertyImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = PropertyImage
        fields = ['image']


class PropertyListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Property
        fields = '__all__'


class RegionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Region
        fields = ['region_name']


class ReviewSerializer(serializers.ModelSerializer):
    created_date = serializers.DateTimeField(format='%d.%m.%Y')
    class Meta:
        model = Review
        fields = [
            'id','buyer',
            'seller','rating','comment','created_date']

class PropertyListSerializer(serializers.ModelSerializer):
    images = PropertyImageSerializer(many=True, read_only=True)
    class Meta:
        model = Property
        fields = ['images','city','title','price','area','rooms','property_type','condition']


class PropertyDetailSerializer(serializers.ModelSerializer):
    images = PropertyImageSerializer(many=True, read_only=True)
    class Meta:
        model = Property
        fields = ['id','title','description','city','region','district','street',
    'area','price','property_type','rooms',
    'floor','total_floors','condition','documents','seller','images',
        ]



class ReviewCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['id','rating','buyer', 'comment', 'seller',]