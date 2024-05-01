from django.views.generic.edit import CreateView, DeleteView, UpdateView, FormView

from .forms import AddEventsForm
from .models import *
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from django.urls import reverse


class EventsView(ListView):
    model = Events
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(EventsView, self).get_context_data(**kwargs)
        return context

class EventsDetail(DetailView):
    model = Events
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(EventsDetail, self).get_context_data(**kwargs)
        return context

class EventsAdd(CreateView):
    # model = Incidents
    form_class = AddEventsForm
    template_name = "events/events_form.html"
    success_url = 'events-detail'

    def get_success_url(self):
        return reverse('events-detail', kwargs={'pk': self.object.pk})

class EventsDelete(DeleteView):
    model = Events
    success_url = '/'

class EventsUpdate(UpdateView):
    model = Events
    form_class = AddEventsForm
    template_name = "events/events_update_form.html"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(EventsUpdate, self).get_context_data(**kwargs)
        return context

    def get_success_url(self):
        return reverse('events-detail', kwargs={'pk': self.object.pk})
