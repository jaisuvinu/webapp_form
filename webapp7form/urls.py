
from django.contrib import admin
from django.urls import path
from myapp1.views import Signin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',Signin)
]
