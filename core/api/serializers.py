from rest_framework import serializers

from core.api.validators import (
    InstitutionValidationMixin,
    UserValidationMixin,
)
from core.models import Institution, User, UserProfile


class UserSerializer(UserValidationMixin, serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name="core-api:user-detail"
    )

    class Meta:
        model = User
        fields = [
            "id",
            "url",
            "created_at",
            "updated_at",
            "username",
            "first_name",
            "last_name",
            "fullname",
            "email",
            "date_of_birth",
            "address",
            "sex",
            "phone_number",
            "institution",
            "role",
        ]

        read_only_fields = [
            "url",
            "id",
            "fullname",
            "role",
            "created_at",
            "updated_at",
        ]


class InstitutionSerializer(
    InstitutionValidationMixin, serializers.ModelSerializer
):
    url = serializers.HyperlinkedIdentityField(
        view_name="core-api:institution-detail"
    )

    class Meta:
        model = Institution
        fields = "__all__"
        read_only_fields = ["id"]


class UserSerializerWithoutInstitution(UserSerializer):
    class Meta(UserSerializer.Meta):
        read_only_fields = UserSerializer.Meta.read_only_fields + [
            "institution"
        ]


class UserProfileSerializer(serializers.ModelSerializer):
    user = UserSerializerWithoutInstitution()

    class Meta:
        model = UserProfile
        fields = ["user", "bio", "avatar"]


class InstitutionProfileSerializer(serializers.ModelSerializer):
    institution = InstitutionSerializer()

    class Meta:
        model = Institution
        fields = ["institution", "bio", "logo"]
