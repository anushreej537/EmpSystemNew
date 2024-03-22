from django.shortcuts import render,redirect
from .forms import EmpForm
from .models import EmpDetail
from django.http import HttpResponse
from django.http import Http404


def index(request):
    return render(request,'index.html')


def addemp(request):
    if request.method == 'POST':
        data = EmpForm(request.POST)
        if data.is_valid():
            data.save()
            return HttpResponse('data stored in database successfully')
    else:
        data = EmpForm()
    return render(request,'addemp.html',{"data":data})

def viewempdata(request):
    data = EmpDetail.objects.all()
    return render(request,'viewempdata.html',{'data':data})

def removeempdata(request,id):
    empdata = EmpDetail.objects.all()
    dataid = EmpDetail.objects.get(id=id).delete()
    return render(request,'viewempdata.html',{'empdata':empdata})

# def removeempdata(request,id):
#     try:
#         # Attempt to retrieve the EmpDetail object with the specified ID
#         emp_detail = EmpDetail.objects.get(id=id)
#         print(emp_detail)
#         # Delete the object
#         emp_detail.delete()
#         # Fetch updated empdata after deletion
#         empdata = EmpDetail.objects.all()
#         # Pass empdata to the template for rendering
#         return render(request, 'removeempdata.html', {'empdata': empdata})
#     except EmpDetail.DoesNotExist:
#         # If the object with the specified ID doesn't exist, raise a 404 error
#         raise Http404("EmpDetail matching query does not exist.")