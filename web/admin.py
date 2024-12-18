from django.contrib import admin
from .models import Workshop, SubWorkshop, Blog, Team, Contact

# Register your models here.

admin.site.register(Workshop)
admin.site.register(SubWorkshop)
admin.site.register(Blog)
admin.site.register(Team)
admin.site.register(Contact)