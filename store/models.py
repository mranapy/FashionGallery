from django.db import models
from django.urls import reverse
from django.core.validators import MaxValueValidator, MinValueValidator

# Category Model
class Category(models.Model):
    category_name = models.CharField(max_length=50,unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    description = models.CharField(max_length=200,blank=True)
    cat_image = models.ImageField(upload_to='photos/categories', blank=True)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'categories'
    def getUrl(self):
        return reverse('store:products_by_category', args=[self.slug])
    def __str__(self):
        return self.category_name
    
# Product Model
class Product(models.Model):
    product_name = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    description = models.TextField(max_length=500,blank=True)
    price = models.IntegerField()
    images = models.ImageField(upload_to='photos/products')
    stock = models.PositiveIntegerField(validators=[MinValueValidator(1)])
    is_available = models.BooleanField(default=True)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    
    category = models.ForeignKey(Category,on_delete=models.CASCADE)

    def __str__(self):
        return self.product_name
    def getUrlProduct(self):
        return reverse('store:product_details', args=[self.category.slug,self.slug])

