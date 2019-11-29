from modeltranslation.translator import register, TranslationOptions
from place.models import CookType, Restaurant


@register(CookType)
class CookTypeTranslationOptions(TranslationOptions):
    fields = ("name",)


@register(Restaurant)
class RestaurantTranslationOptions(TranslationOptions):
    fields = ("name", "description")
