# from django.contrib import admin
#
# # Register your models here.
# from django.apps import apps
#
# models = apps.get_models()
#
# for model in models:
#     try:
#         admin.site.register(model)
#     except:
#         pass
from django.contrib import admin

from .models import OTPCode


@admin.register(OTPCode)
class OTPCodeAdmin(admin.ModelAdmin):
    list_display = ('id', 'code', 'expiration_time')
    search_fields = ('code',)
    list_filter = ('expiration_time',)
    ordering = ('id',)
