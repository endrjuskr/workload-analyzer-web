from django.conf.urls import patterns, url

from workload.views import views_api, views_app


urlpatterns = patterns('',
    url(r'register_machine', views_api.register_machine, name='register_machine'),
    url(r'add_workload', views_api.add_workload, name='add_workload'),
    url(r'^$', views_app.home, name='home'),
    url(r'^register$', views_app.register, name='register'),
    url(r'^login$', 'django.contrib.auth.views.login',
        {'template_name': 'workload/user_mgr/login.html', 'extra_context': {'next': '/workload'}},
        name='login'),
    url(r'^logout$', 'django.contrib.auth.views.logout', {'next_page': '/workload'}, name='logout')
)
