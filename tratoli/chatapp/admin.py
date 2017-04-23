from django.contrib import admin
from .models import ChatMessage

class ChatMessageAdmin(admin.ModelAdmin):
    list_display = ['id', 'text']
    list_filter = ['text',]
    search_fields = ['text',]


admin.site.register(ChatMessage, ChatMessageAdmin)

