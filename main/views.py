from django.shortcuts import render

def show_main(request):
    context = {
        'nama_aplikasi' : 'HaloMo United',
        'name': 'Justin Dwitama Seniang',
        'class': 'PBP D'
    }

    return render(request, "main.html", context)