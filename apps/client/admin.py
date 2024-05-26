from django.contrib import admin

from apps.client.models import Client


@admin.register(Client)
class MailingAdmin(admin.ModelAdmin):
    list_display = ('id', 'firstname', 'lastname', 'email',)
    list_filter = ('firstname',)
    search_fields = ('email',)
