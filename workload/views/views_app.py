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


def get_workload(workload_id):
    workload = Workload.objects.get(pk=workload_id)
    usage_cpu = WorkloadResult.objects.filter(workload=workload).filter(key__startswith='cpu')
    usage_cpu = dict(zip(map(lambda x: x.key, usage_cpu), map(lambda x: x.value, usage_cpu)))
    usage_io = WorkloadResult.objects.filter(workload=workload).filter(key__startswith='io')
    usage_io = dict(zip(map(lambda x: x.key, usage_io), map(lambda x: x.value, usage_io)))
    execution = Execution.objects.filter(workload=workload)
    execution = map(
        lambda x: (x, ExecutionResult.objects.filter(execution=x), ExecutionParam.objects.filter(execution=x)),
        execution)
    return {'workload': workload, 'usage_list': usage_cpu, 'cores': ["all", "1", "2", "3", "4"], 'io_list': usage_io,
            'cpu_types': ["all", "sys", "idle", "soft"],'io_types': ["user", "wait"], 'execution_list': execution}




@login_required
def view_workload(request, workload_id):
    status = ERROR_JS_CODE
    return JsonResponse(
        get_view_status_dictionary(status, render_to_string("workload/workload/view.html", get_workload(workload_id))))

@login_required
def view_workloads(request, workloads):
    status = ERROR_JS_CODE
    w = map(get_workload, workloads)
    return JsonResponse(
        get_view_status_dictionary(status, render_to_string("workload/workload/view.html", { "workloads": w })))


from django.template.defaulttags import register


@register.filter
def get_item(key, dictionary):
    t = ""
    for p in ["AVG", "95", "99"]:
        k = key + "_" + p
        t += "<p>" + p + " - " + dictionary.get(k) + "</p>"
    return


@register.filter
def cpu_usage(arg1, arg2):
    return "cpu_usage_{0}_{1}".format(arg1, arg2)


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
