from django.urls import path, include
from . import views

urlpatterns = [
    path('account/', include('django.contrib.auth.urls'), name='login'),
    path('signup/', views.SignUp.as_view(), name='signup'),
    path('', views.home, name='home')
]