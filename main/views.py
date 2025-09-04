from django.shortcuts import render

def show_main(request):
    context = {
        'app_name': 'main',
        'npm': '2406406742',
        'name': 'Justin Dwitama Seniang',
        'class': 'PBP D',
    }
    return render(request, 'main.html', context)
