from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('admin/', views.panel_administrativo, name="auth"),
    path('inicio/', views.index, name="inicio"),
    path('login/', views.login_page, name="login"),
    path('logout/',views.logout_user, name="logout")
]
