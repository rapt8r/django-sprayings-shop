from django.db import models

# Create your models here.
class Alert(models.Model):
    text = models.CharField(max_length=256)
    is_visible = models.BooleanField(default=False)
    def __str__(self):
        return self.text
class Brand(models.Model):
    name = models.CharField(max_length=64)
    def __str__(self):
        return self.name
class Category(models.Model):
    name = models.CharField(max_length=64)
    def __str__(self):
        return self.name
class Disease(models.Model):
    name = models.CharField(max_length=64)
    description = models.TextField(blank=True)
    def __str__(self):
        return self.name

class Spraying(models.Model):
    name = models.CharField(max_length=64)
    desc = models.TextField(blank=True)
    image = models.ImageField(blank=True, upload_to='product_images/')
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING)
    slug = models.SlugField(blank=True)
    brand = models.ForeignKey(Brand ,blank=True, on_delete=models.DO_NOTHING)
    works_on = models.ManyToManyField(Disease, blank=True)
    featured = models.BooleanField(default=False)
    price = models.DecimalField(decimal_places=2, max_digits=6, blank=True)
    is_available = models.BooleanField()
    show_warning = models.BooleanField()
    is_dangarous_to_enviroment = models.BooleanField()
    is_cancerogenic = models.BooleanField()
    def __str__(self):
        return self.name
    class Meta:
        get_latest_by = ['name']