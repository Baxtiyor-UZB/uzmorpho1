from django.db import models
class wfroottab(models.Model):
    id=models.IntegerField(primary_key=True)
    wf=models.CharField(max_length=25)
    wroot=models.CharField(max_length=25)
    pr=models.CharField(max_length=10)
    sf1=models.CharField(max_length=10)
    sf2=models.CharField(max_length=10)
    sf3=models.CharField(max_length=10)
    sf4=models.CharField(max_length=10)
    idlex=models.IntegerField(null = False)
    idlexroot=models.IntegerField(null = False)
    wfdesc=models.TextField(default='okokok')
    def __str__(self):
        return self.wf