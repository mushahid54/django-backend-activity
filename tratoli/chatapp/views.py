from django.shortcuts import render
from oauth2_provider.ext.rest_framework import permissions, OAuth2Authentication
from rest_framework import viewsets, generics
from rest_framework.response import Response
from .models import ChatMessage
from .serializers import ChatMessageSerializer
from .utils import CustomMetaDataMixin
from django.conf import settings


class ChatMessageViewSet(CustomMetaDataMixin, viewsets.ModelViewSet):
    """
        This is the Merchant CRUD for the admin
    """
    queryset = ChatMessage.objects.all()
    serializer_class = ChatMessageSerializer
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [OAuth2Authentication]

    def get_queryset(self):

        user = self.request.query_params.get("user_id", None)
        sender = self.request.user
        if user != 'undefined' and (user and sender):
            return ChatMessage.objects.filter(is_active=True, receiver_id=user, user_id=sender).order_by('-created_on')
        return ChatMessage.objects.filter(is_active=True).order_by('-created_on')

    def create(self, request, *args, **kwargs):
        data = self.request.data
        data['user_id'] = self.request.user.id
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response({"message": "message created"})


    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        message = instance.text
        instance.is_active = False
        instance.save()
        message = "message '{0}' has been deleted".format(message)
        return Response({"message": message})


class DeleteAllChatMessages(CustomMetaDataMixin, generics.DestroyAPIView):
    """
        This API is made to delete all the messages present
    """

    queryset = ChatMessage.objects.all()
    serializer_class = ChatMessageSerializer
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [OAuth2Authentication]

    def get_queryset(self):
        return ChatMessage.objects.filter(is_active=True)


    def destroy(self, request, *args, **kwargs):
        message = ""
        chat_messages = self.get_queryset().update(is_active=False)
        if chat_messages > 0:
            message = "All the messages has been deleted"
        return Response({"message": message})
