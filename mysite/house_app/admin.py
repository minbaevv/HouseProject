from django.contrib import admin
from django.contrib.auth.models import User

from .models import *

admin.site.register(UserProfile)
admin.site.register(City)
admin.site.register(Region)
admin.site.register(Property)
admin.site.register(PropertyImage)
admin.site.register(Review)