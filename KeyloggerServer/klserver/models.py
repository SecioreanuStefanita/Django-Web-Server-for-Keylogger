from django.db import models

# Create your models here.
class Date(models.Model):
    ip_privat=models.CharField(max_length=45)
    user=models.CharField(max_length=45)
    ip_public=models.CharField(max_length=45)
    loguri=models.TextField()
    def __str__(self):
        return self.ip_privat+" "+self.ip_public+' '+self.user+" "+self.loguri

