from django.contrib import admin

from workload.models import *

admin.site.register(Machine)
admin.site.register(Task)
admin.site.register(Execution)
admin.site.register(ExecutionParam)
admin.site.register(ExecutionResult)
admin.site.register(WorkloadResult)
admin.site.register(Comment)
admin.site.register(Workload)
