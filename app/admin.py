from django.contrib import admin
from app.models import data
# Register your models here.
class dataAdmin(admin.ModelAdmin):
    list_display=('Name','Phone','Email','Password','Confirm_Password')
admin.site.register(data,dataAdmin)
