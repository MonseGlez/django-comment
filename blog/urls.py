from django.urls import path
from . import views
from django.views.static import serve 
from django.conf.urls import url
from django.conf import settings
urlpatterns = [
 
    path('', views.post_new, name='post_new'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new/', views.post_new, name='post_new'),
]
