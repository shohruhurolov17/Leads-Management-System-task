from rest_framework.views import APIView
from apps.leads.serializers import (
    LeadListCreateSerializer, 
    LeadDetailSerializer
)
from rest_framework import status
from apps.shared.pagination import CustomPagination
from apps.shared.response import CustomResponse
from apps.leads.models import Lead
from drf_spectacular.utils import (
    extend_schema,
    OpenApiParameter
)
from drf_spectacular.types import OpenApiTypes
from rest_framework.exceptions import NotFound
from apps.leads.permissions import IsAttorneyOrSuperAdmin
from rest_framework.permissions import AllowAny
from apps.shared.tasks import send_an_email
from drf_spectacular.utils import extend_schema


class LeadListCreateView(APIView):

    serializer_class = LeadListCreateSerializer
    pagination_class = CustomPagination
    permission_classes = [IsAttorneyOrSuperAdmin]

    def get_authenticators(self):
        
        request = self.request

        if request and request.method == 'POST':

            return []
        
        return super().get_authenticators()

    def get_permissions(self):

        request = self.request

        if request and request.method == 'POST':

            return [AllowAny()]

        return super().get_permissions()
        
    def get_queryset(self):

        status = self.request.query_params.get('status')

        queryset = Lead.objects.filter(status=status) if status else Lead.objects.all()

        return queryset

    @extend_schema(
        operation_id='lead_create',
        tags=['lead']
    )
    def post(self, request):

        serializer = self.serializer_class(data=request.data)

        serializer.is_valid(raise_exception=True)

        serializer.save()

        prospect_email = serializer.validated_data['email']

        first_name = serializer.validated_data['email']

        last_name = serializer.validated_data['email']

        full_name = f'{first_name} {last_name}'

        send_an_email.apply_async([
            prospect_email,
            full_name
        ])

        return CustomResponse(
            data=serializer.data,
            status=status.HTTP_201_CREATED
        )
    
    @extend_schema(
        operation_id='lead_list',
        tags=['lead'],
        parameters=[
            OpenApiParameter(
            name='status',
            description='Lead status',
            type=OpenApiTypes.STR,
            location=OpenApiParameter.QUERY
            )
        ]
    )
    def get(self, request):

        paginator = self.pagination_class()

        paginated_queryset = paginator.paginate_queryset(
            queryset=self.get_queryset(),
            request=request
        )

        serializer = self.serializer_class(
            paginated_queryset,
            many=True
        )

        return paginator.get_paginated_response(serializer.data)


class LeadDetailView(APIView):

    serializer_class = LeadDetailSerializer
    permission_classes = [IsAttorneyOrSuperAdmin]

    def get_object(self, id: int):

        try:

            return Lead.objects.get(id=id)
        
        except Lead.DoesNotExist:

            raise NotFound(detail='Lead not found.')
        
    @extend_schema(
        operation_id='lead_retrieve',
        tags=['lead']
    )
    def get(self, request, id: int):

        lead = self.get_object(id)

        serializer = self.serializer_class(lead)

        return CustomResponse(data=serializer.data)

    @extend_schema(
        operation_id='lead_update',
        tags=['lead']
    )
    def patch(self, request, id: int):

        lead = self.get_object(id)

        serializer = self.serializer_class(
            lead, 
            data=request.data, 
            partial=True
        )

        serializer.is_valid(raise_exception=True)

        serializer.save()

        return CustomResponse(
            data=serializer.data, 
            message='Lead updated.'
        )
