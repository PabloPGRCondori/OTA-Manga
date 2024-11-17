from django.contrib import admin
from .models import Manga, Category, Cart, CartItem

# Configura el administrador de Manga
class MangaAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'price', 'stock', 'created_at')
    list_filter = ('categories', 'created_at')
    search_fields = ('title', 'author')
    prepopulated_fields = {'title': ('author',)} 

# Configura el administrador de Categoría
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

# Configura el administrador de Carrito
class CartAdmin(admin.ModelAdmin):
    list_display = ('user', 'created_at')

# Configura el administrador de Elementos del Carrito
class CartItemAdmin(admin.ModelAdmin):
    list_display = ('cart', 'manga', 'quantity')

# Registra los modelos en el panel de administración
admin.site.register(Manga, MangaAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Cart, CartAdmin)
admin.site.register(CartItem, CartItemAdmin)
