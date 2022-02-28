"""solution_log URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import auth
from users.views import login
#from users.views import register_view
from problems.views import home_view, problem_view
from solutions.views import solution_view
from solutions.views import solution_view, problem_table_view, search_problem,solution_list_view, update_list_view, delete_list_view, adopted_solutions_list_view, adopted_solution_view
from django.contrib import admin
from django.urls.conf import path

from users.views import logout_view, register
from django.contrib.auth import views as auth_view
from users import views as users_views
from problems.views import adopt_solutions_view, problem_exists_view
from cittu_report.views import *



urlpatterns = [
    path('admin/', admin.site.urls),
    path('problem', problem_view, name="problem"),
    path('solution/', solution_view, name="solution"),

   path('home/', home_view, name = "home"),
    
    path('register/', users_views.register, name="register"),
    path('', auth_view.LoginView.as_view (template_name= 'users/login.html'), name="login"),
    path('logout/', logout_view, name='logout'),
    path('problem_list/', problem_table_view, name='problem_list'),
    path('enter_solution/<id>/', solution_view, name='solution'),
    path('search_problem', search_problem, name='search-problem'),
    path('solution_list/', solution_list_view, name='solution_list'),
    path('update/<id>/', update_list_view, name='update'),
    path('delete/<id>/', delete_list_view, name='delete'),
    path('adopt_solutions/<id>/', adopt_solutions_view, name='adopt_solutions'),
    path('adopted_solutions_list/', adopted_solutions_list_view, name='adopted_solutions_list'),
    path('adopted_solution/<id>/', adopted_solution_view, name='adopted_solution'),
    path('problem_exists/<id>/', problem_exists_view, name='problem_exists'),
    path('report/', report_view, name='report'),
    path('reportform/', reportform_view, name='reportform'),
    path('collectreport/', collect_report, name='collectreport'),
    path('updatereport/<id>/', update_report_view, name='updatereport'),



]
