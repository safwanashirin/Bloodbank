from django.urls import path
from . import views 
urlpatterns = [
    path('sign', views.sign, name="sign"),
    path('login', views.login, name="login"),
    path('add', views.add, name="add"),
    path('list', views.display, name="display"),
    path('',views.first, name="first"),
    path('logout',views.logout, name="logout")
    

    
]
