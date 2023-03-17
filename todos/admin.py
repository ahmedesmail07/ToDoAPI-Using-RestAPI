from django.contrib import admin
from .models import Todo


class TodoAdminView(admin.ModelAdmin):
    list_display = "title", "body"


admin.site.register(Todo, TodoAdminView)
