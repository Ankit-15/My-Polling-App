
from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'pages/index.html')
def home(request):
	return render(request,'pollster/home.html')
