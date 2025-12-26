from .models import *
from rest_framework import serializers

class UserProfileListSerializers(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['first_name', 'last_name', 'username',]

class UserProfileDetailSerializers(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = '__all__'

class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = '__all__'

class RegionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Region
        fields = ['name_region']

class PropertyListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Property
        fields = ['city', 'price', 'title', ]

class PropertyDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Property
        fields = '__all__'

class PropertyImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = PropertyImage
        fields = '__all__'

class ReViewListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['comment', 'rating', 'property', 'created_date']

class ReViewDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'