from django.contrib import admin
from .models import Events, Registeration, SingleRegistration
# Register your models here.

admin.site.register(Events)
admin.site.register(Registeration)
admin.site.register(SingleRegistration)
