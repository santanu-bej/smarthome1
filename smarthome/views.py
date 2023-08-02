from django.http import JsonResponse,HttpResponse
from django.shortcuts import render
from modelsapp.models import Switch
def get_switch_status(request,switch_name):
    switch = Switch.objects.get(switch_name = switch_name)
    return JsonResponse({f"{switch.switch_name}" : switch.switch_status})

def set_switch_status(request,switch_name):
    if request.method == 'GET':
        status = request.GET.get("status")
        status = False if status =='False' else True
        print(status,type(status))
        switch = Switch.objects.get(switch_name = switch_name)
        switch.switch_status = status
        switch.save()
        return JsonResponse({f"{switch.switch_name}" : switch.switch_status})

def add_switch(request,switch_name):
    switch = Switch(switch_name = switch_name,switch_status = False)
    switch.save()
    return HttpResponse("switch added..")

def show_all_switches(request):
    return render(request,"all_switches.html",{"switches" : Switch.objects.all()})