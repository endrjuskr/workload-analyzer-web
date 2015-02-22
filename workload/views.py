from django.http import HttpResponse
import json
from workload.models import *

REQUEST_METHOD = 'GET'

def index(request):
    return HttpResponse("Workload says hey there world!")

def get_status_dictionary(status):
    return {"status": status}

def request_value(request, key):
    return request.GET[key]

def register_machine(request):
    assert (request.method == REQUEST_METHOD)
    result = get_status_dictionary(False)

    machine = Machine(name="ala", description="asdads")
    machine.save()

    return HttpResponse(json.dumps(result), content_type='application/json')