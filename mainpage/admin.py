from django.contrib import admin
from .models import Certificate, Detail, Contact


class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'body', 'created_on', 'checked')
    list_filter = ('checked', 'created_on')
    search_fields = ('name', 'email', 'subject')
    
# Register your models here.
admin.site.register(Detail)
admin.site.register(Contact)
admin.site.register(Certificate)
