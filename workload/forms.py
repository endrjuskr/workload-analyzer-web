from django.forms import ModelForm
from models import Comment
from workload.models import Workload


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        exclude = ('workload', 'execution', 'pub_date')

    def __init__(self, *args, **kwargs):
        super(CommentForm, self).__init__(*args, **kwargs)


class WorkloadForm(ModelForm):
    class Meta:
        model = Workload

    def __init__(self, *args, **kwargs):
        super(WorkloadForm, self).__init__(*args, **kwargs)
