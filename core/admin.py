from django.contrib import admin
from .models import MainCategory, SubCategory, SubTypeCategory, Product, Cart, Checkout


admin.site.register(MainCategory)
admin.site.register(SubCategory)
admin.site.register(SubTypeCategory)
admin.site.register(Product)
admin.site.register(Cart)
admin.site.register(Checkout)

