from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path("", views.startPage, name="startPage"),
    path("basket", views.basket, name="basket"),
    path("login-user", views.loginUser, name="loginUser"),
    path("register-user", views.registerUser, name="registerUser"),
    path("personal-account", views.personalAccount, name="personalAccount"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)