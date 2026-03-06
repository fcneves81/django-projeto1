from django.shortcuts import render

# Create your views here.
def home(request):
    # return HTTP response
    return render(request, 'recipes/home.html', context={
        'name' : 'Fernando'
    })
