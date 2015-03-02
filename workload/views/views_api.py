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


def create_process(process, workload, date):
    task_model = Task.objects.get(pk=process["type"])
    execution_model = Execution(name=process["name"], task=task_model, workload=workload, run_date=date)
    execution_model.save()
    for c in process["params"]:
        print c
        workload_result = ExecutionParam(execution=execution_model, key=c["key"], value=c["value"])
        workload_result.save()
    print "results"
    for c in process["results"]:
        print c
        workload_result = ExecutionResult(execution=execution_model, key=c["key"], value=c["value"])
        workload_result.save()



def create_workload(task, machine):
    d = time.strptime(task["run_time"], "%a, %d %b %Y %H:%M:%S +0000")
    workload_model = Workload(run_machine=machine, name=task["name"], run_date=d)
    workload_model.save()
    for c in task["usage"]:
        workload_result = WorkloadResult(workload=workload_model, key=c["key"], value=c["value"])
        workload_result.save()
    map(lambda x: create_process(x, workload_model, d), task["processes"])



@csrf_exempt
def add_workload(request):
    assert (request.method == REQUEST_METHOD)
    result = get_status_dictionary(True)
    workload = json.loads(request.body)
    machine = Machine.objects.get(pk=workload["machine"])
    map(lambda x: create_workload(x, machine), workload["tasks"])

    #workload_model = Workload(run_machine=machine, run_date=time.strftime("%H:%M:%S %d/%m/%Y"), name=workload["name"])
    #workload_model.save()

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