from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.urls import reverse
from django.utils.html import format_html

# Register your models here.
from .models import Vehicle, Beneficiary, Contract



class ContractAdmin(admin.ModelAdmin):
    exclude = ('start_kilometer', 'end_kilometer', 'created_by', 'created_at')  # Exclude start_kilometer from the admin form
    # Show all fields in the list view
    list_display = ('vehicle', 'beneficiary', 'start_date', 'end_date', 'status', 'price', 'deposit', 'start_kilometer', 'end_kilometer', 'pdf')
    readonly_fields = ('created_by', 'created_at')

    def pdf(self, obj):
        contract_url = reverse('contract-get-contract-pdf', args=[obj.pk])
        bill_url = reverse('contract-get-bill-pdf', args=[obj.pk])
        return format_html('<a href="{}" target="_blank">Contrat</a> <a href="{}" target="_blank">Facture</a>', contract_url, bill_url)

    pdf.short_description = 'PDF'
    pdf.allow_tags = True





admin.site.register(Vehicle)
admin.site.register(Beneficiary)
admin.site.register(Contract, ContractAdmin)



