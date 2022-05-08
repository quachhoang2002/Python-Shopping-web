from django.contrib import admin
from .models import product,cart,caterogy,order,orderDetail
# Register your models here.
admin.site.register(product)
admin.site.register(cart)
admin.site.register(caterogy)
admin.site.register(order)
admin.site.register(orderDetail)