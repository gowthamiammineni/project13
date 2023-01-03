from django.shortcuts import render

# Create your views here.
def operations(request):
    d={'a':123,'b':107,'c':341}
    return render(request,'operations.html',d)