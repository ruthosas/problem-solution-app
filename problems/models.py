from django.db import models
from django.contrib.auth.models import User

class ProblemType(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title

class Location(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title

class Cause(models.Model):
    problem = models.ForeignKey(ProblemType, on_delete=models.CASCADE)
    cause = models.TextField(null = True, blank=True)

    def __str__(self):
        return self.cause

class App(models.Model):
    app_name = models.CharField(max_length=100)

    def __str__(self):
        return self.app_name

class Title(models.Model):
    title = models.CharField(max_length=100)
    app = models.ForeignKey(App, on_delete=models.CASCADE)


    def __str__(self):
        return self.title

class Problem(models.Model):
    app = models.ForeignKey(App, on_delete=models.CASCADE, blank=True, null=True)
    problem_type = models.ForeignKey(ProblemType, on_delete=models.CASCADE)
    title = models.ForeignKey(Title, on_delete=models.CASCADE)
    description = models.TextField(null = True, blank=True)
    attempted = models.BooleanField(default=False)
    adopted = models.BooleanField(default=False)
    date_created = models.DateTimeField(auto_now_add = True, auto_now=False)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    location = models.ForeignKey(Location, on_delete=models.CASCADE, blank=True)

    def __str__(self):
        return f"{self.title}:   Recorded by {self.created_by} at {self.location}"