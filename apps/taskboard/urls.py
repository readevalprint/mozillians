from django.conf.urls.defaults import patterns, url
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import never_cache

from taskboard.views import CreateTask, EditTask, ListTasks, ViewTask


urlpatterns = patterns('',
    url(r'^new/$', login_required(CreateTask.as_view()),
        name="taskboard_task_new"),
    url(r'^(?P<pk>\d+)/$',
        login_required(never_cache(ViewTask.as_view())),
        name="taskboard_task_detail"),
    url(r'^(?P<pk>\d+)/edit/$',
        login_required(never_cache(EditTask.as_view())),
        name="taskboard_task_edit"),
    url(r'^/$', login_required(ListTasks.as_view()),
        name="taskboard_task_list"),
)
