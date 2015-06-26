from django.contrib import admin
from .models import Certificado


@admin.register(Certificado)
class CertificadoAdmin(admin.ModelAdmin):
    list_display = ('persona', 'desde', 'hasta')
