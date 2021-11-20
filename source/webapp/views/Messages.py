from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseBadRequest
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse
from django.views.generic import CreateView, ListView

from webapp.forms import MessageForm
from webapp.models import Messages


class UserListView(ListView):
    model = get_user_model()
    template_name = 'messages/index.html'
    context_object_name = 'users'
    paginate_by = 10
    paginate_orphans = 4

    def get_queryset(self):
        current_query = super().get_queryset().exclude(pk=self.request.user.pk)
        return current_query


class MessageCreateView(LoginRequiredMixin, CreateView):
    template_name = 'messages/mesage_create.html'
    form_class = MessageForm
    model = Messages

    def form_valid(self, form):
        message = form.save(commit=False)
        message.sender = self.request.user
        message.reciver = get_object_or_404(get_user_model(), pk=self.kwargs.get('pk'))
        if message.sender == message.reciver:
            return HttpResponseBadRequest()
        else:
            message.save()
            return redirect('webapp:sended_message')

    def get_success_url(self):
        return redirect('webapp:sended_message')


class SendedMessages(LoginRequiredMixin, ListView):
    model = Messages
    template_name = 'messages/sended_msg.html'
    context_object_name = 'sended_messages'
    paginate_by = 10
    paginate_orphans = 4

    def get_queryset(self):
        current_query = super().get_queryset().filter(sender=self.request.user).order_by('-pk')
        return current_query


class RecivedMessages(LoginRequiredMixin, ListView):
    model = Messages
    template_name = 'messages/recived_msg.html'
    context_object_name = 'recived_messages'
    paginate_by = 10
    paginate_orphans = 4

    def get_queryset(self):
        current_query = super().get_queryset().filter(reciver=self.request.user).order_by('-pk')
        return current_query
