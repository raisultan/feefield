from django.contrib import admin

from ..models import Fee


@admin.register(Fee)
class FeeAdmin(admin.ModelAdmin):
    ...
