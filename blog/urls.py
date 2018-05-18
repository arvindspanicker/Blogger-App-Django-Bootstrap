from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.home ,name='home'),
    path('profile/', views.profile, name='profile'),
    path('addblog/', views.addblog, name='addblog'),
    path('blog/', views.blog, name='blog'),
    path('chat/', views.chat, name='chat'),
]