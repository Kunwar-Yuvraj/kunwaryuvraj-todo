from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskCreateForm, TaskUpdateForm, ClientForm, TaskLoginForm

from django.views.generic import (
    ListView,
    CreateView,
    DetailView,
    UpdateView,
    DeleteView,
    FormView
)

from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import login


def index(request):
    return render(request, 'index.html')


def index2(request):
    return render(request, 'index2.html')


class CustomLoginView(LoginView):
    redirect_authenticated_user = True
    form_class = TaskLoginForm

    def get_success_url(self):
        return reverse_lazy('task-list')


class RegisterPage(FormView):
    form_class = ClientForm
    success_url = reverse_lazy('task-list')

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(RegisterPage, self).form_valid(form)


    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('task-list')

        return super(RegisterPage, self).get(*args, **kwargs)


class TaskList(LoginRequiredMixin, ListView):
    model = Task
    context_object_name = 'task_list'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['task_list'] = context['task_list'].filter(user=self.request.user)
        context['count_incomplete'] = context['task_list'].filter(complete=False).count()
        context['count_complete'] = context['task_list'].filter(complete=True).count()
        context['count_total'] = context['count_incomplete'] + context['count_complete']

        search_input = self.request.GET.get('search-area') or ''
        if search_input:
            context['task_list'] = context['task_list'].filter(title__startswith=search_input)
        context['search_input'] = search_input



        return context


class TaskCreate(LoginRequiredMixin, CreateView):
    form_class = TaskCreateForm
    model = Task
    success_url = reverse_lazy('task-list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(TaskCreate, self).form_valid(form)


class TaskDelete(LoginRequiredMixin, DeleteView):
    model = Task
    success_url = reverse_lazy('task-list')
    context_object_name = 'task_delete'


class TaskUpdate(LoginRequiredMixin, UpdateView):
    model = Task
    form_class = TaskUpdateForm
    success_url = reverse_lazy('task-list')


class TaskDetail(LoginRequiredMixin, DetailView):
    model = Task
    context_object_name = 'task_detail'
