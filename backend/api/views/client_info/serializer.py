from rest_framework import serializers
from database.models import ClientPersonInfo


class ClientPersonInfoCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClientPersonInfo
        fields = [
            "client_name",
            "client_phone",
            "vacancy",
            "preferred_communication",
            "telegram_username",
        ]

    def validate(self, data):
        preferred_communication = data.get("preferred_communication")
        telegram_username = data.get("telegram_username")

        if (
            preferred_communication == ClientPersonInfo.CommunicateSelect.TELEGRAM
            and not telegram_username
        ):
            raise serializers.ValidationError(
                {
                    "telegram_username": "Для выбранного способа связи 'Telegram' необходимо указать имя пользователя."
                }
            )

        if (
            preferred_communication != ClientPersonInfo.CommunicateSelect.TELEGRAM
            and telegram_username
        ):
            raise serializers.ValidationError(
                {
                    "telegram_username": "Имя пользователя Telegram не требуется для выбранного способа связи."
                }
            )

        return data

    def create(self, validated_data):
        # Создание объекта ClientPersonInfo
        return ClientPersonInfo.objects.create(**validated_data)
