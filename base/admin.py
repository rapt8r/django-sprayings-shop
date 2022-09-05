from django.contrib import admin
from .models import Disease, Spraying, Brand, Category, Alert

# Register your models here.
admin.site.register(Spraying)
admin.site.register(Disease)
admin.site.register(Brand)
admin.site.register(Category)
admin.site.register(Alert)
