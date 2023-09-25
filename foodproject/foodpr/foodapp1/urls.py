from . import views
from django.urls import path

app_name='foodapp1'

urlpatterns = [

    path('register',views.fun1,name='register'),
    path('login',views.login,name='login'),
    path('logout',views.logout,name='logout')

]