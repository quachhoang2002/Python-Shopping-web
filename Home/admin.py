from django.contrib import admin
from .models import product,cart,caterogy,order
# Register your models here.
admin.site.register(product)
admin.site.register(cart)
admin.site.register(caterogy)
admin.site.register(order)