from django.contrib import admin

# Register your models here.
from .models import District,Branch

class DistricAdmin(admin.ModelAdmin):
    list_display = ['name']
admin.site.register(District,DistricAdmin)


class BranchAdmin(admin.ModelAdmin):
    list_display = ['name']
admin.site.register(Branch,BranchAdmin)