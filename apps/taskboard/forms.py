from groups.forms import GroupField
from django import forms
from taskboard.models import Task
from tower import ugettext as _, ugettext_lazy as _lazy
from ajax_select.fields import AutoCompleteSelectField


class TaskForm(forms.ModelForm):
    # TODO - Make contacts (users) autocomplete
    groups = GroupField(required=False)
    instructions = forms.CharField(widget=forms.Textarea(attrs={'placeholder': _('Tell us all about it...')}))
    contact = AutoCompleteSelectField('userprofile', required=False, help_text=None)

    class Meta:
        model = Task

    def save(self, commit=True):
        """Sync the groups from the form and DB keeping system groups."""
        # have to use commit=False to avoid it automatically adding and
        # removing groups.
        print "TaskForm.save() called"
        print ''
        task = super(TaskForm, self).save(commit=False)
        task.save()
        # not using task.save_m2m b/c that would blindly remove
        # system tasks.

        # Remove any non-system groups that weren't supplied in this list.
        task.groups.remove(*[g for g in task.groups.all()
                             if g not in self.cleaned_data['groups']
                             and not g.system])
        # Add any non-system groups from the form
        task.groups.add(*[g for g in self.cleaned_data['groups']
                          if not g.system])
        return task
