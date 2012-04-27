from django.conf.urls.defaults import patterns, url
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import never_cache
from forms import TaskForm
from models import Task
from taskboard import views
from django.views.generic.edit import CreateView
from django.conf.urls.defaults import *

urlpatterns = patterns('',
    url(r'^new/$', views.CreateTask.as_view(),
        name="new_task"),
    url(r'^(?P<slug>[a-z0-9-]+)/$',
        login_required(never_cache(views.ViewTask.as_view())),
        name="view_task"),
    url(r'^(?P<slug>[a-z0-9-]+)/edit/$',
        login_required(never_cache(views.EditTask.as_view())),
        name="edit_task"),
    url(r'^(?P<slug>[a-z0-9-]+)/take/$', views.take_task, name="take_task"),
    url(r'^(?P<slug>[a-z0-9-]+)/release/$', views.release_task, name="release_task"),
    url(r'^$', login_required(views.ListTasks.as_view()),
        name="list_tasks"),
)
