from django.contrib import admin

# Register your models here.
from .models import Contact, Product, About, Land

admin.site.register(Contact)
admin.site.register(Product)
admin.site.register(About)
admin.site.register(Land)