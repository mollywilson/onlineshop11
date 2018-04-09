from django.http import HttpResponse

def index(request):
    return HttpResponse("<h1> This is the cart app homepage </h1>")