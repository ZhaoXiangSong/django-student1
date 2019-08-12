from django.urls import path
from . import views
urlpatterns = [
    path('index/',views.index,name='index'),
    path('register/',views.register,name='register'),
    path('register_check/',views.register_check),
    path('do_register/',views.do_register,name='do_register'),
    path('login/',views.login,name='login'),
    path('do_login/',views.do_login,name='do_login'),
    path('logout/',views.logout,name='logout'),
    path('User1/',views.User1,name='User1'),
    # path('http://192.168.119.119:5000/award/',views.img),
]