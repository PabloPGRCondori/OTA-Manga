from rest_framework import serializers
from .models import Manga, Category, Cart, CartItem

# Serializador de Categoría
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

# Serializador de Manga
class MangaSerializer(serializers.ModelSerializer):
    categories = CategorySerializer(many=True, read_only=True)

    class Meta:
        model = Manga
        fields = '__all__'

# Serializador de Elemento en el Carrito
class CartItemSerializer(serializers.ModelSerializer):
    manga = MangaSerializer(read_only=True)  # Serializamos el objeto Manga

    class Meta:
        model = CartItem
        fields = ['id', 'manga', 'quantity', 'get_total_price']

# Serializador de Carrito de Compras
class CartSerializer(serializers.ModelSerializer):
    items = CartItemSerializer(many=True, read_only=True)  # Serializamos los elementos del carrito

    class Meta:
        model = Cart
        fields = ['id', 'user', 'items', 'created_at']
