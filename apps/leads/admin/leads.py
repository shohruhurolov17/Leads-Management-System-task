from apps.leads.models import Lead
from django.contrib import admin
from unfold.admin import ModelAdmin


@admin.register(Lead)
class LeadAdmin(ModelAdmin):

    model = Lead
    list_display = ('first_name', 'last_name', 'email', 'status', 'resume')
