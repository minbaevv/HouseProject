import django_filters
from django_filters import FilterSet
from .models import Property

class PropertyFilter(FilterSet):
    class Meta:
        model = Property
        fields = {
            'city': ['exact'],
            'region': ['exact'],
            'district': ['exact',],
            'property_type': ['exact'],
            'condition': ['exact'],
            'rooms': ['exact',],
            'floor': ['exact', 'gt', 'lt'],
            'price': [ 'gt', 'lt'],
            'area': [ 'gt', 'lt'],
            'documents': ['exact'],
            'seller': ['exact'],
        }
