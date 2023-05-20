from rest_framework.serializers import ModelSerializer, HyperlinkedIdentityField
from django.contrib.auth import get_user_model

User = get_user_model()


class UserSerializer(ModelSerializer):
    user_detail_url = HyperlinkedIdentityField(
        view_name="user-detail", read_only=True, lookup_field="pk"
    )

    class Meta:
        model = User
        exclude = (
            "groups",
            "user_permissions",
            "password",
        )
