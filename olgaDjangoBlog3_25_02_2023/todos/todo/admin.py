from django.contrib import admin
from .models import Todo

class TodoAdmin(admin.ModelAdmin):
    readonly_field = ('created',)

admin.site.register(Todo, TodoAdmin)
