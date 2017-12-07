from django.shortcuts import render

# Create your views here.
def index(request):
    d = [1,2,3,4]
    return render(request, 'index.html', {'test': d})
