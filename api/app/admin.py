from django.contrib import admin
from .models import InputText
# Register your models here.

# register
@admin.register(InputText)
class InputText(admin.ModelAdmin):
    pass
