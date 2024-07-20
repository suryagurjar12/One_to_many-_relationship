from django.db import models

# Create your models here.
class Department(models.Model):
    dep_name=models.CharField(max_length=50)
    dep_dis=models.CharField(max_length=50)
    
    def __str__(self):
        return self.dep_name
    
class Student(models.Model):
    Name=models.CharField(max_length=50)
    Email=models.EmailField()
    Contact=models.IntegerField()
    dep_name=models.ForeignKey(Department,on_delete=models.CASCADE)
    
    def __str__(self):
        return self.Name+' '+str(self.dep_name)
    
