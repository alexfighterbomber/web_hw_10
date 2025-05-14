from django.contrib import admin

from django.contrib import admin
from .models import UserQuote

@admin.register(UserQuote)
class UserQuoteAdmin(admin.ModelAdmin):
    list_display = ('quote', 'author', 'user', 'approved')
    list_editable = ('approved',)  
    list_filter = ('approved',)
    actions = ['approve_quotes']

    def approve_quotes(self, request, queryset):
        queryset.update(approved=True)
    approve_quotes.short_description = "Схвалити обрані цитати"