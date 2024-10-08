from django.urls import path
from User_app import views
from django.contrib.auth import views as auth_views



urlpatterns = [
    path('register', views.register, name="register" ),
    path('login', auth_views.LoginView.as_view(), name="login" ),
    # path('logout', auth_views.LogoutView.as_view(template_name = 'logout.html'), name="logout" ),
    path('logout', views.logout_view, name="logout" ),
]