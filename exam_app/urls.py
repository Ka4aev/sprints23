from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('', views.index,name='home'),
    path('register/', views.RegisterView.as_view(), name='register'),
    path('login', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('profile/', views.Profile.as_view(), name='profile'),
    path('service/', views.ServiceList.as_view(), name='service_list'),
    path('service/<int:pk>/', views.ServiceDetail.as_view(), name='service_detail'),
    path('service/<int:pk>/order/', views.create_order, name='create_order'),
]