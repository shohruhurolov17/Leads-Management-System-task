from rest_framework.views import APIView
from apps.users.serializers import LoginSerializer, UserDetailSerializer
from apps.shared.response import CustomResponse
from drf_spectacular.utils import extend_schema

class LoginView(APIView):

    authentication_classes = []
    permission_classes = []
    serializer_class = LoginSerializer


    @extend_schema(
        operation_id='auth_login',
        tags=['auth']
    )
    def post(self, request):

        serializer = self.serializer_class(
            data=request.data, 
            context={'request': request}
        )

        serializer.is_valid(raise_exception=True)

        user = serializer.validated_data['user']

        data = UserDetailSerializer(user).data

        return CustomResponse(data=data)
