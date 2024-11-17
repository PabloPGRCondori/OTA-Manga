from django.db import models
from django.contrib.auth.models import User

# Modelo de Categoría
class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

# Modelo de Manga
class Manga(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField()  # Número de unidades disponibles
    description = models.TextField()
    cover_image = models.ImageField(upload_to='covers/')
    categories = models.ManyToManyField(Category, related_name='mangas')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

# Modelo de Carrito de Compras
class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Carrito de {self.user.username}"

# Modelo de Elemento en el Carrito de Compras
class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='items')
    manga = models.ForeignKey(Manga, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.quantity} x {self.manga.title}"

    # Método para calcular el precio total de los artículos en el carrito
    def get_total_price(self):
        return self.quantity * self.manga.price
