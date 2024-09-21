
from django.contrib import admin
from django.urls import path, include
from Tasklistapp import views as todolistapp_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', todolistapp_views.index, name="index" ),
    path('list/',  include("Tasklistapp.urls")),
    path('Account/',  include("User_app.urls")),
    path("about/", todolistapp_views.about, name="about us" ),
    path("contact/", todolistapp_views.contact, name="contact us" ),
]
