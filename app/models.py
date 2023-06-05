from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Question(models.Model):
    
    
    
    question = models.TextField()
    option1 = models.CharField(max_length=100)
    option2 = models.CharField(max_length=100)
    option3 = models.CharField(max_length=100)
    option4 = models.CharField(max_length=100)
    ans = models.CharField(max_length=50,null=True, blank=True)
    

class Answer(models.Model):
    
    ans = models.CharField(max_length=50,null=True, blank=True)
    fk_Question = models.ForeignKey(Question,on_delete=models.CASCADE,null=True, blank=True)
    fk_user = models.ForeignKey(User,on_delete=models.CASCADE,null=True, blank=True)
    mark = models.FloatField()
    

