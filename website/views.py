from django.shortcuts import render

def Load_Index(request):
    return render(request , 'index.html')
