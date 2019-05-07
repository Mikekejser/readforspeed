from django.contrib import admin
from .models import Text, UserText


@admin.register(Text)
class TextAdmin(admin.ModelAdmin):
	list_display = ('text',)


@admin.register(UserText)
class UserTextAdmin(admin.ModelAdmin):
	list_display = ('user', 'title')