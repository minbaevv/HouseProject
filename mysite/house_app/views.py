from .models import UserProfile, City, Region, Property, Review, PropertyImage
from .serializers import (UserProfileListSerializers, UserProfileDetailSerializers,
                          CitySerializer, RegionSerializer, PropertyListSerializer,
                          PropertyDetailSerializer, ReViewListSerializer, ReViewListSerializer, PropertyImageSerializer)
from rest_framework import viewsets, generics

class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileListSerializers

class CityViewSet(viewsets.ModelViewSet):
    queryset = City.objects.all()
    serializer_class = CitySerializer

class RegionViewSet(viewsets.ModelViewSet):
    queryset = Region.objects.all()
    serializer_class = RegionSerializer

class PropertyViewSet(viewsets.ModelViewSet):
    queryset = Property.objects.all()
    serializer_class = PropertyListSerializer

class PropertyImageViewSet(viewsets.ModelViewSet):
    queryset = PropertyImage.objects.all()
    serializer_class = PropertyImageSerializer

class ReViewListViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReViewListSerializer

