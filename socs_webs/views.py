from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'socs_webs/index.html')
def events(request):
    return render(request, 'socs_webs/events.html')
def contact(request):
    return render(request, 'socs_webs/contact.html')