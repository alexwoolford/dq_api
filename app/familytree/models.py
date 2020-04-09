from django.db import models


class Parent(models.Model):
    class Meta:
        db_table = "parent"
    firstname = models.CharField(max_length=60)
    lastname = models.CharField(max_length=60)
    age = models.IntegerField()


class Child(models.Model):
    class Meta:
        db_table = "child"
    firstname = models.CharField(max_length=60)
    middlename = models.CharField(max_length=60, null=True, blank=True)
    lastname = models.CharField(max_length=60)
    age = models.IntegerField()
    parent = models.ForeignKey(Parent, on_delete=models.CASCADE,
                               related_name="children")

    def __str__(self):
        return '%s: %s' % (self.firstname, self.lastname)
