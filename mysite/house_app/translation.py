from .models import City, Region, Property, Review, UserProfile
from modeltranslation.translator import TranslationOptions,register


@register(UserProfile)
class ProductTranslationOptions(TranslationOptions):
    fields = ('first_name', 'last_name', 'username')


@register(City)
class ProductTranslationOptions(TranslationOptions):
    fields = ('city_name',)

@register(Region)
class ProductTranslationOptions(TranslationOptions):
    fields = ('region_name',)

@register(Property)
class ProductTranslationOptions(TranslationOptions):
    fields = ('title', 'description',)

@register(Review)
class ProductTranslationOptions(TranslationOptions):
    fields = ('comment',)