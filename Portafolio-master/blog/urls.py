from tabnanny import verbose
from django.urls import path 
from blog import views
from .views import render_posts, post_detail

app_name = 'blog'

urlpatterns = [
    path('', render_posts, name='posts'),
    path('<int:post_id>/',post_detail, name="post_detail"),
]


# Panel de administracion



