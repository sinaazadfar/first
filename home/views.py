from django.shortcuts import render
# Create your views here.
 
def home(request):
    context = {
        "name": "Sina"
    }
    return render(request,"home\home.html",context)
