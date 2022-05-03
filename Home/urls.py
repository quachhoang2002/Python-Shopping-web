from django.urls import path
from unicodedata import name
from . import views
from django.conf import settings
from django.conf.urls.static import static
app_name= 'home'
urlpatterns = [
    path('',views.index,name='index'),
    path('login',views.Login,name='Login'),
    path('logout',views.Logout,name='Logout')
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
