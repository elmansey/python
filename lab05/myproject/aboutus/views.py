from django.shortcuts import render

# Create your views here.
def aboutusPage(request):
    return render(request, 'aboutusPage.html')