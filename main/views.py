from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'index.html')

def aboutus(request):
    return render(request, 'aboutus.html')

def contact(request):
    return render(request, 'contact.html')

def gallery(request):
    return render(request, 'gallery.html')

def menu(request):
    return render(request, 'menu.html')

def elements(request):
    return render(request, 'elements.html')

def contact_process(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        # Here you can process the form, e.g., send email
        # For now, just redirect back
        return render(request, 'contact.html', {'success': True})
    return render(request, 'contact.html')
