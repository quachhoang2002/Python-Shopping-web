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
    path('orderForm',views.Order_Form,name='order-form'),
    path('Detail/<str:id>',views.ProductDetail,name='ProductDetail'),
    path('bill/',views.bill,name="bill"),
    path("updateCart/>", views.updateCart, name="update-cart"),
    path('delete/<str:product_id>',views.deleteCart,name='delete-cart'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
