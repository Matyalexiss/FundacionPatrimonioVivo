from django.shortcuts import render


def home(request):
    print("Metodo del request: "+ request.method)
    
    data = {
        
    }
    return render(request, 'core/home.html', data)