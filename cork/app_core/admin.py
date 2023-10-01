from django.contrib import admin
from .models import Ticket, Location, Regularity, ToValidate

admin.site.register(Ticket)
admin.site.register(Location)
admin.site.register(Regularity)
admin.site.register(ToValidate)
