from rest_framework import serializers
from .models import ChatMessage

class ChatMessageSerializer(serializers.ModelSerializer):

    created_on = serializers.DateTimeField(format="%d %b %y %I:%M %p", read_only=True)

    class Meta:
        model = ChatMessage
        fields = ('id', 'text', 'created_on', 'user_id', 'receiver_id')

    def create(self, validated_data):
        validated_data['user_id'] = self.initial_data.get('user_id')
        validated_data['receiver_id'] = self.initial_data.get('received_id')
        return ChatMessage.objects.create(**validated_data)