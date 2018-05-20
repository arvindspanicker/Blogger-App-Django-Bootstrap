from django.urls import path, include , re_path
from . import views
urlpatterns = [
    path('', views.home ,name='home'),
    path('profile/', views.profile, name='profile'),
    path('addblog/', views.addblog, name='addblog'),
    re_path('editblog/(?P<id>\w{0,50})', views.editblog, name='editblog'),
    re_path('blog/(?P<id>\w{0,50})', views.blog, name='blog'),
    path('chat/', views.chat, name='chat'),
]