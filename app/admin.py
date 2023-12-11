from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(Contact)
admin.site.register(Slider)
admin.site.register(About)

class ImagesInline(admin.StackedInline):
    model = Image
    extra = 1

@admin.register(Classes)
class ClassesAdmin(admin.ModelAdmin):
    inlines = [ImagesInline]