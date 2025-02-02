from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("about/", views.about, name="about"),
    path("contact/", views.contact, name="contact"),
    path("demo/", views.demo, name="demo"),
    path("updates/", views.updates, name="updates"),

]

