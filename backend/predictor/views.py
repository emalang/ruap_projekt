from django.shortcuts import render

def home(request):
    # za početak samo prikaz stranice
    return render(request, "predictor/home.html")
