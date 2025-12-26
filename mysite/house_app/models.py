from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator, MaxValueValidator
from phonenumber_field.modelfields import PhoneNumberField

class UserProfile(AbstractUser):
    age = models.PositiveSmallIntegerField(validators=[MinValueValidator(18), MaxValueValidator(80)], null=True,
                                           blank=True)
    phone_number = PhoneNumberField(null=True, blank=True)
    ROLE_CHOICES = (
        ('seller', 'seller'),
        ('buyer', 'buyer'))
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)
    role = models.CharField(choices=ROLE_CHOICES,max_length=16,default='buyer')

    def __str__(self):
        return f'{self.first_name} {self.last_name}, {self.username}'


class City(models.Model):
    city_name = models.CharField(max_length=30)

    def __str__(self):
        return f'{self.city_name}'

class Region(models.Model):
    region_name = models.CharField(max_length=30)

    def __str__(self):
        return f'{self.region_name}'


class Property(models.Model):
    PROPERTY_TYPE_CHOICES = (
        ('apartment', 'apartment'),
        ('house', 'house'),
        ('land', 'land'),
        ('commercial', 'commercial'),
    )
    CONDITIONS = (
        ('new', 'New'),
        ('good', 'Good'),
        ('needs_repair', 'Needs repair'),
    )
    title = models.CharField(max_length=100)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    region = models.ForeignKey(Region, on_delete=models.CASCADE)
    district = models.CharField(max_length=100,null=True,blank=True)
    street = models.CharField(max_length=150,null=True,blank=True)
    area = models.DecimalField(max_digits=8,decimal_places=2,null=True,blank=True)
    price = models.PositiveIntegerField()
    property_type = models.CharField(max_length=50,choices=PROPERTY_TYPE_CHOICES)
    rooms = models.PositiveIntegerField()
    floor = models.PositiveIntegerField()
    total_floors = models.PositiveIntegerField()
    condition = models.CharField(max_length=20, choices=CONDITIONS)
    documents = models.BooleanField(default=False)
    seller = models.ForeignKey(UserProfile,on_delete=models.CASCADE)
    description = models.TextField(max_length=500,null=True,blank=True)

    def __str__(self):
        return f'{self.title} ({self.get_property_type_display()}) — {self.city}, Хозяин: {self.seller}'


class PropertyImage(models.Model):
    property = models.ForeignKey(Property, on_delete=models.CASCADE,related_name='images')
    image = models.ImageField(upload_to='property_images')

    def __str__(self):
        return f'{self.property}, {self.image}'


class Review(models.Model):
    buyer = models.ForeignKey(UserProfile,on_delete=models.CASCADE)
    seller = models.ForeignKey(UserProfile, related_name='reviews', on_delete=models.CASCADE, null=True, blank=True)
    rating = models.PositiveIntegerField(choices=[(i, str(i)) for i in range(1, 6)])
    comment = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.buyer} {self.seller} {self.rating}'



