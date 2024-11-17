from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MangaViewSet, CategoryViewSet, CartViewSet, CartItemViewSet

router = DefaultRouter()
router.register(r'mangas', MangaViewSet)
router.register(r'categories', CategoryViewSet)
router.register(r'carts', CartViewSet)
router.register(r'cart-items', CartItemViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
