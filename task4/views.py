from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
def service(request):
    return render(request, 'fourth_task/service.html')


def in_work(request):
    devices = ['Принтеры HP', 'Сканеры HP', 'МФУ HP']
    context = {
        # 'title' : title,
        'devices' : devices,
    }
    return render(request, 'fourth_task/in_work.html', context)

def ready(request):
    return render(request, 'fourth_task/ready.html',)