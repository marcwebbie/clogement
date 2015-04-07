from django.contrib import admin

from .models import Cahier, Pays, Ville, Logement


class LogementAdmin(admin.ModelAdmin):
    model = Logement


class LogementInline(admin.TabularInline):
    model = Logement
    extra = 0
    fields = ['ville', 'prix']


class CahierAdmin(admin.ModelAdmin):
    model = Cahier
    inlines = [LogementInline]


class PaysAdmin(admin.ModelAdmin):
    model = Pays


class VilleAdmin(admin.ModelAdmin):
    model = Ville


admin.site.register(Cahier, CahierAdmin)
admin.site.register(Pays, PaysAdmin)
admin.site.register(Ville, VilleAdmin)
admin.site.register(Logement, LogementAdmin)
