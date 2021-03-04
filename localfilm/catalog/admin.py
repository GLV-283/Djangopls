from django.contrib import admin
from .models import filmini

class filminiAdmin(admin.ModelAdmin):
    list_display = ('title', 'tagline',  'popularity', 'overview')


admin.site.register(filmini, filminiAdmin)
