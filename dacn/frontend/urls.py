from  django.urls import path
from .import views
from django.contrib.auth import views as auth_views
app_name = 'frontend'
urlpatterns = [
    #index
    path('',views.index, name='index'),
     #/discount/id
    path('<id>/',views.single,name='single'),
    #/category/category_name
    path('category/<name>',views.category,name='category'),
    #/signup
    path('signup',views.signup,name='signup'),
    #/logout
    path('logout',views.logout,name='logout'),
    # #/login
    # path('login',auth_views.login,{'template_name': 'header.html'},name='login')
]
