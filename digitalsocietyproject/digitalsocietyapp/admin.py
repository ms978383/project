from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(User)
admin.site.register(Secretory)
admin.site.register(Member)
admin.site.register(Notice)
admin.site.register(Event)