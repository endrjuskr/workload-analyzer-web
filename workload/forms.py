from django.forms import ModelForm
from models import Comment


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        exclude = ('workload', 'execution', 'pub_date')

    def __init__(self, *args, **kwargs):
        super(CommentForm, self).__init__(*args, **kwargs)
