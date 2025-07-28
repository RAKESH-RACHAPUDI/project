"""
URL configuration for studentmanagement project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from application.views import landingpage
from application.views import adddetails
from application.views import showdetails
from application.views import update
from application.views import delete
from application.views import user_login
from application.views import register_view
from application.views import logout_view



urlpatterns = [
     path('admin/', admin.site.urls),
    path("", landingpage, name='landingpage'),
    path("adddetails", adddetails, name="adddetails"),
    path("showdetails", showdetails, name='showdetails'),
    path("update/<int:id>/", update, name='update'),  
    path("delete/<int:id>/", delete, name='delete1'),
    path('login/', user_login, name='login'),
    path('register/', register_view, name='registerpage'),
    path('logout/', logout_view, name='logout'),
   
   
]
