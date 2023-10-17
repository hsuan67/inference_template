import pandas as pd
from django.shortcuts import render, HttpResponse, redirect
from django.views.decorators.http import require_POST
from .forms import FileForm

# Create your views here.
@require_POST
def inference(request):
    form = FileForm(request.POST, request.FILES)
    if not form.is_valid(): 
        print(form.errors)
        return redirect('home:index')

    # save tmp file
    file_obj = form.save()
    file_name = file_obj.file.name
    file_pth = file_obj.file.path

    # Run your code
    ## result = inference(file_pth)

    # delte tmp file
    file_obj.delete()

    result_val = "Done"
    context = {
        'result':result_val
    }
    return render(request, 'inference/result.html', context)


def test(request):
    context = {
        'filename':"test",
        'filepth':"./"
    }
    return render(request, 'inference/result.html', context)