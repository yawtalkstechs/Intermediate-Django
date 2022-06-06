from django.shortcuts import HttpResponse

# Create your views here.
def home_page_view(request):
    return HttpResponse("Hello World!")