from django.contrib import admin
from phonebook.models import PhoneNumber

class PhoneNumberAdmin(admin.ModelAdmin):
    model = PhoneNumber
    list_editable = 'number name'.split()
    list_display = 'id number name'.split()
    search_fields = 'number name'.split()

admin.site.register(PhoneNumber, PhoneNumberAdmin)
