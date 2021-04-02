from django.db import models
#create model class for Django university classes
class djangoClasses(models.Model):
    Title = models.CharField(max_length=60, default="", blank=True, null=False)
    courseNumber = models.IntegerField(max_length=5)
    instructorName = models.CharField(max_length=60, default="", blank=True, null=False)
    duration = models.DecimalField(default=0.00, max_digits=10000,decimal_places=2)
#add model manager named objects
    objects = models.Manager()

