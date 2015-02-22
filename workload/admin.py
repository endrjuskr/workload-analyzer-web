from django.contrib import admin

from workload.models import Machine, Task, Execution, ExecutionParam, Workload

admin.site.register(Machine)
admin.site.register(Task)
admin.site.register(Execution)
admin.site.register(ExecutionParam)
admin.site.register(Workload)
