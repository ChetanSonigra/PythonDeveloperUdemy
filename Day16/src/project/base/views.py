from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render, redirect
#from django.http import HttpResponse
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .models import Task
# Create your views here.

#def pending_list(request):
#    return HttpResponse('Pending List')
class Login(LoginView):
    template_name='base/login.html'
    fields ='__all__'
    redirect_authenticated_user = True
    
    def get_success_url(self) -> str:
        return reverse_lazy('pending_list')

class RegisterPage(FormView):
    template_name='base/register.html'
    form_class= UserCreationForm
    redirect_authenticated_user = True
    success_url=reverse_lazy('pending_list')
    
    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request,user)
        return super(RegisterPage,self).form_valid(form)
    
    def get(self,*args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('pending_list')
        return super(RegisterPage,self).get(*args,**kwargs)
        
class PendingList(LoginRequiredMixin,ListView):
    model = Task
    context_object_name = 'tasks'
    def get_context_data(self, **kwargs) -> dict[str]:
        context = super().get_context_data(**kwargs)
        context["tasks"] = context["tasks"].filter(user=self.request.user)
        context["count"] = context["tasks"].filter(completed=False).count()
        search_value = self.request.GET.get('search-area') or ''
        if search_value:
            context["tasks"] = context["tasks"].filter(title__icontains=search_value)
        context['search_value']= search_value
        return context
    
class TaskDetail(LoginRequiredMixin,DetailView):
    model = Task
    context_object_name = 'task_detail'
    template_name = 'base/task.html'
    
class CreateTask(LoginRequiredMixin,CreateView):
    model = Task
    fields = ['title', 'description','completed'] # or '__all__'
    success_url = reverse_lazy('pending_list')
    
    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        form.instance.user = self.request.user
        return super(CreateTask,self).form_valid(form)
    
class EditTask(LoginRequiredMixin,UpdateView):
    model = Task
    fields = ['title','description','completed']
    success_url = reverse_lazy('pending_list')
    
class DeleteTask(LoginRequiredMixin,DeleteView):
    model = Task
    context_object_name = 'task'
    success_url = reverse_lazy('pending_list')