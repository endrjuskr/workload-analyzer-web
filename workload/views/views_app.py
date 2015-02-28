from django.shortcuts import render, HttpResponseRedirect
from django.template.loader import render_to_string
from django.contrib.auth.forms import UserCreationForm

from workload.models import Workload


def home(request):
    if request.user.is_authenticated():
        home_content = get_registered_home_content(request)
    else:
        home_content = render_to_string('workload/front_pages/unregistered_home.html')
    return render(request, 'workload/layout.html', {'home_content': home_content})


def view_workload(request):
    if request.user.is_authenticated():
        home_content = get_registered_home_content(request)
    else:
        home_content = render_to_string('workload/front_pages/unregistered_home.html')
    return render(request, 'workload/layout.html', {'home_content': home_content})


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