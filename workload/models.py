from django.db import models
from datetime import datetime, timedelta


class Machine(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=400)
    processor_name = models.CharField(max_length=200, default="")
    available_memory = models.CharField(max_length=200, default="")
    swap_memory = models.CharField(max_length=200, default="")

    def __unicode__(self):
        return u'%s' % (self.name)


class Task(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=200)

    def __unicode__(self):
        return u'%s' % (self.name)


class Workload(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    measurement_type = models.IntegerField()
    run_date = models.DateTimeField('run date', default=datetime.now())
    run_machine = models.ForeignKey(Machine)

    def __unicode__(self):
        return u'%s (%s , %s)' % (self.name, str(self.run_date), str(self.measurement_type))


class Execution(models.Model):
    run_date = models.DateTimeField('run date', default=datetime.now())
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    task = models.ForeignKey(Task)
    workload = models.ForeignKey(Workload)

    def __unicode__(self):
        return u'%s (%s)' % (self.name, str(self.run_date))


class Comment(models.Model):
    execution = models.ForeignKey(Execution, blank=True, null=True)
    workload = models.ForeignKey(Workload, blank=True, null=True)
    author = models.CharField(max_length=200)
    content = models.CharField(max_length=200)
    pub_date = models.DateTimeField('publish date', default=datetime.now())

    def __unicode__(self):
        return u'%s %s' % (self.author, str(self.pub_date))


class ExecutionParam(models.Model):
    execution = models.ForeignKey(Execution)
    value = models.CharField(max_length=200)
    key = models.CharField(max_length=200)

    def __unicode__(self):
        return u'%s - %s' % (self.key, self.value)


class WorkloadResult(models.Model):
    workload = models.ForeignKey(Workload)
    value = models.CharField(max_length=200)
    key = models.CharField(max_length=200)

    def __unicode__(self):
        return u'%s - %s' % (self.key, self.value)


class ExecutionResult(models.Model):
    execution = models.ForeignKey(Execution)
    value = models.CharField(max_length=200)
    key = models.CharField(max_length=200)

    def __unicode__(self):
        return u'%s - %s' % (self.key, self.value)

