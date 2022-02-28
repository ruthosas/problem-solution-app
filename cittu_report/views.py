from django.shortcuts import render, redirect
from.models import *
from .forms import *
from django.contrib import messages

# Create your views here.
def report_view(request):
    report = SubUnitReport.objects.all()
    context = {'report':report} 
    return render(request, 'report.html', context)


def reportform_view(request):
    form = ReportForm()

    if request.method=='POST':
        form = ReportForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('report')
    context={'form':form}        
    return render(request, 'reportform.html', context )


def collect_report(request):
    collect_report=None
    report_types = ReportType.objects.all()
    print(report_types)

    get_report_type = request.GET.get('report_type')
    date_from = request.GET.get('date_from')
    date_to = request.GET.get('date_to')

    if request.method == 'GET':
        if not get_report_type:
            messages.info(request, "Please select Report type and specify date range")
        else:
            collect_report = SubUnitReport.objects.filter(
                report_type_id=get_report_type,
                date_from__gte=date_from, date_to__lte=date_to
                )

    context = {'collect_report': collect_report, "report_types":report_types}
    return render(request, 'collectreport.html', context)

def update_report_view(request, id):
    reports = SubUnitReport.objects.get(id=id)
    form = ReportForm(instance=reports)  

    if request.method=='POST':
        form = ReportForm(request.POST, request.FILES, instance=reports)  
        if form.IS_valid():
            form.save()
        return redirect ('collectreport')

    context = {'reports': reports, 'form':form}
    return render(request, 'reportform.html', context)
    


 