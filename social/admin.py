from django.contrib import admin
from .models import Link

@admin.register(Link)
class LinkAdmin(admin.ModelAdmin):
    readonly_fields = ('create', 'altered')
    list_display = ('chave', 'create', 'altered')
