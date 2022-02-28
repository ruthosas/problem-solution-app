from django.shortcuts import render, redirect, get_object_or_404
from solutions.models import Solution
from solutions.forms import SolutionForm

from problems.models import Problem
from django.contrib.auth.decorators import login_required

@login_required
def solution_view(request, id):
    problem = Problem.objects.get(id=id)

    if request.method == 'POST':
        solution_var = request.POST.get('solution')
        if solution_var != '':
            obj = Solution.objects.create(
                problem_id = problem.id,
                solution = solution_var,
                created_by = request.user
            )
            obj.save()
            Problem.objects.filter(id=id).update(attempted=True)
            return redirect('/problem_list')
        else:
            print('No Solution')
            
    template = 'solutions/solutions.html'
    context = {"problem":problem}
    return render(request, template, context)


@login_required
def problem_table_view(request):
    problems = Problem.objects.filter(adopted=False)

    template = 'solutions/problem_table.html'
    context = {"problems":problems}
    return render(request, template, context)

def solution_list_view(request):
    problems = Problem.objects.filter(adopted=False)

    template = 'solutions/solution_list.html'
    context = {"problems":problems}
    return render(request, template, context)

@login_required
def update_list_view(request,id):
    obj = Solution.objects.get(id=id)
    if request.method == 'POST':
        solution = request.POST.get("solution")
        Solution.objects.filter(id=id).update(solution=solution)
        return redirect ('solution_list')
   
    template = 'solutions/update.html'
    context = {"obj":obj }
    return render(request, template, context)
    

def search_problem(request):
    if request.method=='POST':
        searched = request.POST.get('searched', None)
        problems = Problem.objects.filter(description__icontains=searched)
        template = 'search/search_problem.html'
        context = {'searched':searched, 'problems':problems}
        return render(request, template, context)
    else:
        return render(request, 'search/search_problem.html', {})

def delete_list_view(request, id):
    obj = get_object_or_404(Solution, id=id)
    if request.method == 'POST':
        obj.delete()
        return redirect('solution_list')
   
    template = 'solutions/delete.html'
    context = {"obj":obj}
    return render(request, template, context)

def adopted_solutions_list_view(request):
    problems = Problem.objects.filter(adopted=True)

    template = 'solutions/adopted_solutions_list.html'
    context = {"problems":problems}
    return render(request, template, context)
    
def adopted_solution_view(request, id):
    problem = Problem.objects.get(id=id)

    template = 'solutions/adopted_solution.html'
    context = {"problem":problem}
    return render(request, template, context)


    


