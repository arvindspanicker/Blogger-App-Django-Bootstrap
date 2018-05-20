from django.urls import path, include , re_path
from . import views
urlpatterns = [
    path('', views.home ,name='home'),
    path('profile/', views.profile, name='profile'),
    path('addblog/', views.addblog, name='addblog'),
    re_path('editblog/(?P<id>\w{0,50})', views.editblog, name='editblog'),
    re_path('blog/(?P<id>\w{0,50})', views.blog, name='blog'),
    re_path('chat/(?P<room_name>\w{0,50})', views.chat, name='chat'),
    re_path('like/(?P<id>\w{0,50})', views.like, name = 'like'),
    re_path('notification/(?P<room_name>\w{0,50})', views.shownotification, name = 'shownotification'),
]