
from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin

from django.core.paginator import Paginator
from django.shortcuts import redirect, render
from django.views.generic import DetailView, CreateView, UpdateView, DeleteView, ListView
from django.urls import reverse, reverse_lazy

from webapp.models import Jopening
from webapp.forms import JopeningForm


class JIndexView(ListView):
    model = Jopening
    template_name = 'jopening/index.html'
    ordering = ['created_at']
    paginate_by = 5
    context_object_name = 'jopenings'


class JopeningView(DetailView):
    model = Jopening
    template_name = 'jopening/jopening_view.html'


class JopeningCreateView(LoginRequiredMixin, CreateView):
    model = Jopening
    form_class = JopeningForm
    template_name = 'jopening/jopening_create.html'

    def get_success_url(self):
        return reverse('webapp:jopening_view', kwargs={'pk': self.object.pk})

    def form_valid(self, form):
        jopening = form.save(commit=False)
        jopening.author = self.request.user
        jopening.save()
        return redirect('webapp:jopening_view', pk=jopening.pk)


class JopeningUpdateView(PermissionRequiredMixin, UpdateView):
    model = Jopening
    form_class = JopeningForm
    template_name = 'jopening/jopening_update.html'
    permission_required = 'webapp.change_jopening'

    def has_permission(self):
        jopening = self.get_object()
        return super().has_permission() or jopening.author == self.request.user

    def get_success_url(self):
        return reverse('webapp:jopening_view', kwargs={'pk': self.object.pk})


class JopeningDeleteView(PermissionRequiredMixin, DeleteView):
    model = Jopening
    template_name = 'jopening/jopening_delete.html'
    success_url = reverse_lazy('webapp:j_index')
    permission_required = 'webapp.delete_jopening'

    def has_permission(self):
        jopening = self.get_object()
        return super().has_permission() or jopening.author == self.request.user
