from django.urls import path
from django.contrib.auth.views import LogoutView
from . import views
urlpatterns=[
    path('',views.home,name="home"),
    path('logout/', views.logout_view, name='logout')
]