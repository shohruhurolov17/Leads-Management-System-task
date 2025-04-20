from django.urls import path
from apps.leads.views import (
    LeadListCreateView,
    LeadDetailView
)

urlpatterns = [
    path('v1/leads', LeadListCreateView.as_view(), name='lead_create_list'),
    path('v1/leads/<str:id>', LeadDetailView.as_view(), name='lead_detail')
]