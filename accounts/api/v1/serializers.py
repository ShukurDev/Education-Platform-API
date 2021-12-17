from rest_framework import serializers

from accounts.models import User


class AccountsSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"
