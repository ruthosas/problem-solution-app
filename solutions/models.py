from django.db import models
from django.contrib.auth.models import User
from problems.models import Problem

class Solution(models.Model):
    problem = models.ForeignKey(Problem, on_delete=models.CASCADE)
    solution = models.TextField(max_length=200, null=False, blank=False)
    date_created = models.DateTimeField(auto_now_add = True, auto_now=False)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    
    def __str__(self):
        return self.solution
        
        #f"{self.problem}:   Solved by {self.created_by} on the {self.date_created}"
        
    
