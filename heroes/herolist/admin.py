from django.contrib import admin

# Register your models here.
from .models import Hero, Synergy

admin.site.register(Hero)
admin.site.register(Synergy)