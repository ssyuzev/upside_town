from django.contrib import admin

from .models import Person, Like


@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    pass


@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    pass
