from django.contrib import admin

from .models import App, Cause, ProblemType, Problem, Location, Title

admin.site.register(Problem)
admin.site.register(ProblemType)
admin.site.register(Location)
admin.site.register(Cause)
admin.site.register(App)
admin.site.register(Title)

