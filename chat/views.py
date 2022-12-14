from django.forms import FloatField
from django.shortcuts import render
from rest_framework import generics
from rest_framework import permissions
# Create your views here.
from django.db import models
from chat.models import Chat, Message
from common.models import User
from chat import serializers


class ChatListView(generics.ListAPIView):
    queryset = Chat.objects.all().annotate(
        last_message=Message.objects.filter(
            chat_id=models.OuterRef('id')).order_by('-created_at').values('text')[:1],
        last_message_date=Message.objects.filter(
            chat_id=models.OuterRef('id')).order_by('-created_at').values('created_at')[:1]
    )
    serializer_class = serializers.ChatListSerializer
    permission_classes = (permissions.IsAuthenticated, )
# .order_by("-messages__created_at").distinct()

    def get_queryset(self):
        return self.queryset.filter(members=self.request.user).annotate(
            # profile image
            profile_image=models.Case(
                models.When(is_group=True, then=models.F('avatar')),
                models.When(is_group=False, then=User.objects.exclude(
                    id=self.request.user.id).filter(chat__title=models.OuterRef('title')).values('avatar')[:1]),
                default=models.Value('None image'),
                output_field=models.CharField()
            ),
            # profile title
            profile_title=models.Case(
                models.When(is_group=True, then=models.F('title')),
                models.When(is_group=False, then=User.objects.exclude(
                    id=self.request.user.id).filter(chat__title=models.OuterRef('title')).values('full_name')[:1]),
                default=models.Value('None image')

            ),
            is_unmuted=models.Case(
                models.When(unmuted=self.request.user, then=True),
                default=False,
                output_field=models.BooleanField()
            ),
            is_pinned=models.Case(
                models.When(pinned=self.request.user, then=True),
                default=False,
                output_field=models.BooleanField()
            ),
            is_read=models.Case(
                models.When(messages__read=self.request.user, then=True),
                default=False,
                output_field=models.BooleanField()
            ),

        ).order_by("-messages__created_at").order_by("-is_pinned")
