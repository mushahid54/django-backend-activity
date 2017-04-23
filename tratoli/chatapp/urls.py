from django.conf.urls import url
from .views import DeleteAllChatMessages

urlpatterns = [
    url(r'^delete-all-messages/$', DeleteAllChatMessages.as_view(), name='delete-all-messages')

]
