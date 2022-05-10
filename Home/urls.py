from django.urls import path
from unicodedata import name
from . import views
from django.conf import settings
from django.conf.urls.static import static
app_name= 'home'
urlpatterns = [  
    path('',views.home,name='home'),
    path('product/',views.Shopping,name='Shopping'),
    path('contract/',views.contract,name='contract'),
    path('login',views.Login,name='Login'),
    path('logout',views.Logout,name='Logout'),
    path('register',views.Register,name='Register'),
    path('addtoCart/',views.addtoCart,name='addtoCart'),
    path('cart/',views.Cart,name='Cart'),
    path('order/',views.Order,name='order'),
    path('orderForm',views.Order_Form,name='order-form'),
    path('Detail/<str:id>',views.ProductDetail,name='ProductDetail'),
    path('bill/',views.bill,name="bill"),
    path("updateCart/>", views.updateCart, name="update-cart"),
    path('delete/<str:product_id>',views.deleteCart,name='delete-cart'),
    path('showDetail/',views.order_detail,name='order_detail'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
