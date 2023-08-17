from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.signup,name='signup'),
    path('login/',views.login_page,name='login'),
    path('home/',views.home,name='home'),
    path('logout/',views.logout_page,name='logout'),
]
