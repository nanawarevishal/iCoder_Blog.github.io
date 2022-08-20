from django.contrib import admin
from home.models import Contact
# Register your models here.



class MyContact(admin.ModelAdmin):
    list_display = ('sno','name','phone','email','desc','password')

admin.site.register(Contact,MyContact)
