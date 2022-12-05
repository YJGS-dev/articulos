from django.shortcuts import render

# Create your views here.

def articulo_screen_view(request):
    context = {}
    return render(request, "articulo.html", context)