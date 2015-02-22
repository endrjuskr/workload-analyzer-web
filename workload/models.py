from django.db import models


class Machine(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=200)

    def __unicode__(self):
        return u'%s' % (self.name)


class Task(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=200)

    def __unicode__(self):
        return u'%s' % (self.name)


class Comment(models.Model):
    run_date = models.DateTimeField('run date')
    author = models.CharField(max_length=200)
    content = models.CharField(max_length=200)
    pub_date = models.DateTimeField('publish date')


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


class ExecutionParam(models.Model):
    execution = models.ForeignKey(Execution)
    value = models.CharField(max_length=200)
    key = models.CharField(max_length=200)

    def __unicode__(self):
        return u'%s - %s' % (self.key, self.value)
