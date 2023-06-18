from django.urls import path
from . import views

urlpatterns = [
    path('', views.About_Us, name='aboutus'),
    path('profiles/', views.Profiles, name ='profiles'),
    path('portfolio/', views.portfolio, name ='protfolio'),
    path('usercreateform/', views.usercfrm, name ='usercform'),
    path('login/', views.login_form, name ='login'),
    path('success/', views.slogin, name ='slogin'),
    path('logout/', views.logout_form, name ='logout'),
    path('changepass/', views.change_password, name ='changepass'),
    path('withoutoldpass/', views.change_without_old_password, name ='withoutoldpass'),
]