from django.urls import path
from .views import register, dashboard, shorten_link, redirect_link, home, about

urlpatterns = [
    path('', home, name='home'),
    path('register/', register, name='register'),
    path('dashboard/', dashboard, name='dashboard'),
    path('shorten/', shorten_link, name='shorten_link'),
    path('r/<str:name>/', redirect_link, name='redirect_link'),
    path('about/', about, name="about")
]
