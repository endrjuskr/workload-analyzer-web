from dajaxice.decorators import dajaxice_register
from django.http import JsonResponse

from constants import *
from utils import get_view_status_dictionary
from views.views_app import get_registered_home_content


@dajaxice_register
def dashboard_ajax(request):
    return JsonResponse(get_view_status_dictionary(OK_JS_CODE, get_registered_home_content(request)))

@dajaxice_register(method=REQUEST_METHOD_GET, name='workload.view_workload')
def view_workload_ajax(request, form=None):
    return view_workload(request, form)