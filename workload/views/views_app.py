from django.core.exceptions import ValidationError
from django.shortcuts import render, HttpResponseRedirect
from django.template.loader import render_to_string
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from workload.forms import CommentForm, WorkloadForm
from dajaxice.utils import deserialize_form
from workload.utils import get_view_status_dictionary
from django.http import JsonResponse

from workload.models import Workload, Execution, WorkloadResult, ExecutionResult, ExecutionParam

from django.template import RequestContext

from workload.constants import *


def home(request):
    if request.user.is_authenticated():
        home_content = get_registered_home_content(request)
    else:
        home_content = render_to_string('workload/front_pages/unregistered_home.html')
    return render(request, 'workload/layout.html', {'home_content': home_content})


@login_required
def new_workload_comment(request, workload_id, form=None):
    status = ERROR_JS_CODE
    if request.method == REQUEST_METHOD_POST:
        comment_form = CommentForm(data=deserialize_form(form))
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.workload = Workload.objects.get(pk=workload_id)
            new_comment.save()
            return JsonResponse(get_view_status_dictionary(OK_JS_CODE, get_registered_home_content(request)))
        return JsonResponse(
            get_view_status_dictionary(status, "Something went wrong"))
    else:
        comment_form = CommentForm()
        return JsonResponse(
            get_view_status_dictionary(status, render_to_string("workload/comments/new_workload_comment.html",
                                                                {'form': comment_form, 'workload_id': workload_id},
                                                                context_instance=RequestContext(
                                                                    request))))


@login_required
def new_execution_comment(request, execution_id, form=None):
    status = ERROR_JS_CODE
    if request.method == REQUEST_METHOD_POST:
        comment_form = CommentForm(data=deserialize_form(form))
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.execution = Execution.objects.get(pk=execution_id)
            new_comment.save()
            return JsonResponse(get_view_status_dictionary(OK_JS_CODE, get_registered_home_content(request)))
        return JsonResponse(
            get_view_status_dictionary(status, "Something went wrong"))
    else:
        comment_form = CommentForm()
        return JsonResponse(
            get_view_status_dictionary(status, render_to_string("workload/comments/new_execution_comment.html",
                                                                {'form': comment_form, 'execution_id': execution_id},
                                                                context_instance=RequestContext(
                                                                    request))))


@login_required
def view_workload(request, workload_id):
    status = ERROR_JS_CODE
    workload = Workload.objects.get(pk=workload_id)

    usage = WorkloadResult.objects.filter(workload=workload, key__startwith='cpu')
    execution = Execution.objects.filter(workload=workload)
    execution = map(lambda x: (x, ExecutionResult.objects.filter(execution=x), ExecutionParam.objects.filter(execution=x)), execution)
    return JsonResponse(get_view_status_dictionary(status, render_to_string("workload/workload/view.html",
                                                                            {'workload': workload, 'usage_list':usage, 'execution_list':execution },
    )))


def register(request):
    if request.method == 'POST':
        usr_form = UserCreationForm(request.POST)
        return HttpResponseRedirect("/")
    else:
        usr_form = UserCreationForm()

    return render(request, 'workload/user_mgr/register.html', {'form': usr_form})


def get_registered_home_content(request):
    return render_to_string("workload/front_pages/registered_home.html", {
        'workload_list': Workload.objects.all()})
