from django.urls import path
from unicodedata import name
from . import views
from django.conf import settings
from django.conf.urls.static import static
app_name= 'home'
urlpatterns = [
    path('',views.index,name='index'),
    path('login',views.Login,name='Login'),
    path('logout',views.Logout,name='Logout'),
    path('register',views.Register,name='Register'),
    path('addtoCart/<str:product_id>',views.addtoCart,name='addtoCart'),
    path('cart/',views.Cart,name='Cart'),
    path('order/',views.Order,name='order'),
    path('orderForm',views.Order_Form,name='order-form')
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
