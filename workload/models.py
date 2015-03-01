from django.db import models


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
    run_date = models.DateTimeField('run date')
    run_machine = models.ForeignKey(Machine)

    def __unicode__(self):
        return u'%s (%s)' % (self.name, str(self.run_date))


class Execution(models.Model):
    run_date = models.DateTimeField('run date')
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    task = models.ForeignKey(Task)
    workload = models.ForeignKey(Workload)

    def __unicode__(self):
        return u'%s (%s)' % (self.name, str(self.run_date))


class Comment(models.Model):
    execution = models.ForeignKey(Execution)
    workload = models.ForeignKey(Workload)
    author = models.CharField(max_length=200)
    content = models.CharField(max_length=200)
    pub_date = models.DateTimeField('publish date')

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
    workload = models.ForeignKey(Workload)
    value = models.CharField(max_length=200)
    key = models.CharField(max_length=200)

    def __unicode__(self):
        return u'%s - %s' % (self.key, self.value)

