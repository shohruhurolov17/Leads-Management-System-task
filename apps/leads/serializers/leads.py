from rest_framework import serializers
from apps.leads.models import Lead


class LeadListCreateSerializer(serializers.ModelSerializer):

    class Meta:

        model = Lead
        fields = (
            'id',
            'first_name',
            'last_name',
            'email',
            'resume',
            'status',
            'created_time'
        )
        read_only_fields = (
            'status', 
            'created_time'
        )


class LeadDetailSerializer(serializers.ModelSerializer):

    class Meta:

        model = Lead
        fields = (
            'id',
            'first_name',
            'last_name',
            'email',
            'resume',
            'status',
            'created_time'
        )
        read_only_fields = ('first_name', 'last_name', 'email', 'resume')
