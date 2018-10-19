import logging

from django.contrib.auth import get_user_model
from rest_framework.serializers import ModelSerializer

LOG = logging.getLogger('core')


class UserSerializer(ModelSerializer):

    class Meta:
        model = get_user_model()
        fields = (
            'id',
            # 'created',
            # 'modified',
            'username',
            'password',
            # 'account_type',
            # 'is_api_user',
            'first_name',
            'last_name',
            'name',
            'connections',
            # 'last_login',
            # 'account_status',
            # 'account_status_updated',
            # 'phone_number',
            # 'avatar',
            # 'role',
        )
        extra_kwargs = {
            'password': {'write_only': True, 'required': False},
            # 'api_token': {'read_only': True},
        }
