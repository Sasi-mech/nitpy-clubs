from django.contrib import admin
from .models import Club, ClubImage, ContactMessage

class ClubImageInline(admin.TabularInline):
    model = ClubImage
    extra = 1

@admin.register(Club)
class ClubAdmin(admin.ModelAdmin):
    inlines = [ClubImageInline]

@admin.register(ClubImage)
class ClubImageAdmin(admin.ModelAdmin):
    pass

@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'created_at')
    search_fields = ('name', 'email', 'subject')
    list_filter = ('created_at',)