from dajaxice.decorators import dajaxice_register
from django.http import JsonResponse

from constants import *
from utils import get_view_status_dictionary
from workload.views.views_app import view_workload, get_registered_home_content, new_workload_comment, \
    new_execution_comment


@dajaxice_register
def dashboard_ajax(request):
    return JsonResponse(get_view_status_dictionary(OK_JS_CODE, get_registered_home_content(request)))


@dajaxice_register(method=REQUEST_METHOD_GET, name='workload.view_workload')
def view_workload_ajax(request, workload_id, form=None):
    return view_workload(request, workload_id, form)


@dajaxice_register(method=REQUEST_METHOD_POST, name='workload.add_workload_comment_submit')
@dajaxice_register(method=REQUEST_METHOD_GET, name='workload.add_workload_comment_form')
def add_workload_comment_ajax(request, workload_id, form=None):
    return new_workload_comment(request, workload_id, form)


@dajaxice_register(method=REQUEST_METHOD_POST, name='workload.add_execution_comment_submit')
@dajaxice_register(method=REQUEST_METHOD_GET, name='workload.add_execution_comment_form')
def add_execution_comment_ajax(request, execution_id, form=None):
    return new_execution_comment(request, execution_id, form)
