from django.http import HttpResponse
import json, time
from django.views.decorators.csrf import csrf_exempt
from workload.models import *

REQUEST_METHOD = 'POST'


def index(request):
    return HttpResponse("Workload says hey there world!")


def get_status_dictionary(status):
    return {"status": status}


def request_value(request, key):
    return request.POST[key]


@csrf_exempt
def add_workload_comment(request):
    assert (request.method == REQUEST_METHOD)
    result = get_status_dictionary(True)

    print request.body
    comment = json.loads(request.body)['comment']

    workload = Workload.objects.get(pk=comment['workload_id'])

    comment_model = Comment(workload=workload,
                            content=comment['content'],
                            author=comment['author'],
                            pub_date=time.strptime(comment['pub_date'], '%d %m %y'))

    comment_model.save()

    return HttpResponse(json.dumps(result), content_type='application/json')


@csrf_exempt
def add_execution_comment(request):
    assert (request.method == REQUEST_METHOD)
    result = get_status_dictionary(True)

    print request.body
    comment = json.loads(request.body)['comment']

    execution = Execution.objects.get(pk=comment['execution_id'])

    comment_model = Comment(execution=execution,
                            content=comment['content'],
                            author=comment['author'],
                            pub_date=time.strptime(comment['pub_date'], '%d %m %y'))

    comment_model.save()

    return HttpResponse(json.dumps(result), content_type='application/json')


@csrf_exempt
def register_machine(request):
    assert (request.method == REQUEST_METHOD)
    result = get_status_dictionary(True)

    machine = json.loads(request.body)
    machine = machine['machine']

    machine_model = Machine(name=machine['name'],
                            processor_name=machine['processor_name'],
                            available_memory=machine['available_memory'],
                            swap_memory=machine['swap_memory'])

    machine_model.save()

    result["machine_id"] = machine_model.id

    return HttpResponse(json.dumps(result), content_type='application/json')


@csrf_exempt
def get_machine(request):
    assert (request.method == REQUEST_METHOD)
    result = get_status_dictionary(True)

    machine = json.loads(request.body)
    machine = machine['machine']

    machine_model = Machine.objects.get(name=machine)

    result["machine_id"] = machine_model.id

    return HttpResponse(json.dumps(result), content_type='application/json')