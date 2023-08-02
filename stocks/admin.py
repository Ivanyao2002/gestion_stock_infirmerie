from django.contrib import admin

from .models import Travailleurs, Medicaments

# Register your models here.

@admin.register(Travailleurs)
class TravailleurAdmin(admin.ModelAdmin):
    pass


@admin.register(Medicaments)
class MedicamentAdmin(admin.ModelAdmin):
    pass
