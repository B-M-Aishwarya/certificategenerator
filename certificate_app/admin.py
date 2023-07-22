from django.contrib import admin
from certificate_app.models import Certificate, VerificationToken

admin.site.site_header = "Certificate | Admin"

class CertificateAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'content', 'created_at']

admin.site.register(Certificate, CertificateAdmin)
admin.site.register(VerificationToken)