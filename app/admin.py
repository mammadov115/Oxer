from django.contrib import admin
from django.http.request import HttpRequest
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


@admin.register(About)
class AboutAdmin(admin.ModelAdmin):

    def has_add_permission(self, request: HttpRequest) -> bool:
        is_empty = About.objects.count() == 0
        return True if is_empty else False


class ImagesInline(admin.StackedInline):
    model = Image
    extra = 1


@admin.register(Classes)
class ClassesAdmin(admin.ModelAdmin):
    inlines = [ImagesInline]

    def has_add_permission(self, request):
        is_empty = Classes.objects.count() == 0
        return True if is_empty else False

    
@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ["title", "created_at", "show_at_home"]


@admin.register(FeedBackSection)
class FeedBackSectionAdmin(admin.ModelAdmin):

    def has_add_permission(self, request):
        is_empty = FeedBackSection.objects.count() == 0
        return True if is_empty else False


admin.site.register(FeedBack)


@admin.register(InfoSection)
class InfoSectionAdmin(admin.ModelAdmin):

    def has_add_permission(self, request):
        is_empty = InfoSection.objects.count() == 0
        return True if is_empty else False

admin.site.register(Message)
admin.site.register(SocialMediaAccount)

@admin.register(BlogsSection)
class BlogsSectionAdmin(admin.ModelAdmin):

    def has_add_permission(self, request):
        is_empty = BlogsSection.objects.count() == 0
        return True if is_empty else False
    
