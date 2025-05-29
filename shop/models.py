from django.db import models
class Category(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name
    
# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.IntegerField()
    category=models.ForeignKey(Category, on_delete=models.CASCADE,related_name='products')
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name
    @property
    def category_name(self):
        return self.category.name