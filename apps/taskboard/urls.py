from django.conf.urls.defaults import patterns, url
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import never_cache
from forms import TaskForm
from models import Task
from taskboard.views import CreateTask, EditTask, ListTasks, ViewTask
from django.views.generic.edit import CreateView
from django.conf.urls.defaults import *
from tastypie.api import Api
from taskboard.api import TaskResource

v1_api = Api(api_name='v1')
v1_api.register(TaskResource())


urlpatterns = patterns('',
    url(r'^api/', include(v1_api.urls)),
    url(r'^new/$', CreateTask.as_view(),
        name="new_task"),
    url(r'^(?P<pk>\d+)/$',
        login_required(never_cache(ViewTask.as_view())),
        name="view_task"),
    url(r'^(?P<pk>\d+)/edit/$',
        login_required(never_cache(EditTask.as_view())),
        name="edit_task"),
    url(r'^$', login_required(ListTasks.as_view()),
        name="list_tasks"),
)
