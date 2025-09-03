from django.shortcuts import render

def show_main(request):
    context = {
        'npm' : '2406359203',
        'name': 'Matthew Wijaya',
        'class': 'PBP C'
    }

    return render(request, "main.html", context)
