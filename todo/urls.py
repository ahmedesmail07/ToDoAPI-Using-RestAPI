from django.contrib import admin
from django.urls import path, include

urlpatterns = [path("admin/", admin.site.urls), path("", include("todos.urls"))]
# here i set the home page as a url of the todos app
