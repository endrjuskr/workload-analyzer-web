from django.conf.urls import patterns, url
from workload import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'register_machine', views.register_machine, name='register_machine')
)
