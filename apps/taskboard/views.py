from django.views.generic import CreateView, UpdateView, ListView, DetailView

from funfactory.urlresolvers import reverse
from taskboard.forms import TaskForm
from taskboard.models import Task


class CreateTask(CreateView):
    form_class = TaskForm
    template_name = 'taskboard/edit_task.html'
    model = Task

    def get_success_url(self):
        # had to do this instead of just defining success_url because it
        # seems that URLs aren't yet ready when this module is first imported
        return reverse('list_tasks')


class EditTask(UpdateView):
    form_class = TaskForm
    template_name = 'taskboard/edit_task.html'
    model = Task
    context_object_name = 'task'

    def get_context_data(self, **kwargs):
        context = super(EditTask, self).get_context_data(**kwargs)
        context['cancel_url'] = reverse('view_task',
                                        kwargs={'pk': self.object.pk})
        return context

    def get_success_url(self):
        return reverse('view_task', kwargs={'pk': self.object.pk})


class ViewTask(DetailView):
    model = Task
    template_name = 'taskboard/view_task.html'


class ListTasks(ListView):
    queryset = Task.objects.filter(disabled=False)
    template_name = 'taskboard/list_tasks.html'
