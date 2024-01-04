from django.contrib import admin
from .models import *
from django.contrib.admin import AdminSite

# Register your models here.


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['number', 'email', 'location']

    def has_add_permission(self, request) -> bool:
        is_empty = Contact.objects.count() == 0
        return True if is_empty else False


@admin.register(Slider)
class Slider(admin.ModelAdmin):
    list_display = ['text']
    ordering = ['id']


admin.site.register(About)


class ImagesInline(admin.StackedInline):
    model = Image
    extra = 1


@admin.register(Classes)
class ClassesAdmin(admin.ModelAdmin):
    inlines = [ImagesInline]


admin.site.register(Blog)
admin.site.register(FeedBackSection)
admin.site.register(FeedBack)
admin.site.register(InfoSection)
admin.site.register(Message)
admin.site.register(SocialMediaAccount)