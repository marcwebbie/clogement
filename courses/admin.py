from django.contrib import admin
from hvad.admin import TranslatableAdmin
from .models import Course, Module, Unit, Challenge


class ChallengeAdmin(TranslatableAdmin):
    model = Challenge


class CourseAdmin(TranslatableAdmin):
    model = Course


class ModuleAdmin(TranslatableAdmin):
    model = Module


class UnitAdmin(TranslatableAdmin):
    model = Unit


class ChallengeAdmin(TranslatableAdmin):
    model = Challenge


admin.site.register(Course, CourseAdmin)
admin.site.register(Module, ModuleAdmin)
admin.site.register(Unit, UnitAdmin)
admin.site.register(Challenge, ChallengeAdmin)
