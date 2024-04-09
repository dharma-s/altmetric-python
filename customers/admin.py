from django.contrib import admin

# Register your models here.
from accounts.models import CustomUser
from .models import Plan

admin.site.register(CustomUser)
admin.site.register(Plan)
