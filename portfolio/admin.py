from django.contrib import admin
from .models import Project, ContactMessage, About


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
	list_display = ('title', 'url', 'created_at')
	search_fields = ('title', 'description')


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
	list_display = ('name', 'email', 'created_at')
	search_fields = ('name', 'email', 'message')


admin.site.register(About)
