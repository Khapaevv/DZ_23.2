from catalog.models import Product, Category
from django.core.cache import cache
from config.settings import CACHE_ENABLED


def get_category_from_cache():
    """Получает данные по категориям из кэша, если кэш пуст, получает данные из БД"""
    if not CACHE_ENABLED:
        return Category.objects.all()
    key = "category_list"
    category = cache.get(key)
    if category is not None:
        return category
    category = Category.objects.all()
    cache.set(key, category)
    return category
