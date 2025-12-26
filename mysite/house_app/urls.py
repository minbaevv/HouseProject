from django.urls import path, include
from rest_framework import routers
from .views import (UserProfileViewSet, CityViewSet, RegionViewSet, PropertyViewSet,
                    PropertyImageViewSet, ReViewListViewSet)

router = routers.DefaultRouter()
router.register(r'users', UserProfileViewSet)
router.register(r'cities', CityViewSet)
router.register(r'regions', RegionViewSet)
router.register(r'property', PropertyViewSet)
router.register(r'property_image', PropertyImageViewSet)
router.register(r'review', ReViewListViewSet)

urlpatterns = [
    path('', include(router.urls))
]