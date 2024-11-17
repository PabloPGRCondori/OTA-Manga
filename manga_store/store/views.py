from rest_framework import viewsets
from .models import Manga, Category, Cart, CartItem
from .serializers import MangaSerializer, CategorySerializer, CartSerializer, CartItemSerializer

# Vista para manejar las operaciones con Mangas
class MangaViewSet(viewsets.ModelViewSet):
    queryset = Manga.objects.all()
    serializer_class = MangaSerializer

# Vista para manejar las operaciones con Categorías
class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

# Vista para manejar las operaciones con Carritos
class CartViewSet(viewsets.ModelViewSet):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer

# Vista para manejar las operaciones con Elementos del Carrito
class CartItemViewSet(viewsets.ModelViewSet):
    queryset = CartItem.objects.all()
    serializer_class = CartItemSerializer
