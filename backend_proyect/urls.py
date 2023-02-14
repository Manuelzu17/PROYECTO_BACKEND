"""backend_proyect URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

# login app
from userAdmin.views import UserAdmin
from loginU.views import UserLoginView, UserLogout
from home.views import HomeView

urlpatterns = [
   path('', HomeView.as_view()),     # new
    path('home/', HomeView.as_view()),
    path('admin/', admin.site.urls),
    path('login/', UserLoginView.as_view(), name="login"),
    path('user/admin/', UserAdmin.as_view(), name="usersAdmin"),
    path('logout/', UserLogout.as_view(), name="logout"),
]
