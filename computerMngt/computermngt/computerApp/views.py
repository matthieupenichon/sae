from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from computerApp.models import Machine,Personne


"""def index(request):
    context = {}
    return render(request, 'template/index.html', context)
"""


def index(request):
    machines = Machine.objects.all()

    context = {
        'machine': machines }
    return render(request, 'template/index.html' ,context=context)

def index ( request ) :
    context = {}
    return render(request, 'index.html', context)






def machine_list_view(request) :
    machines = Machine.objects.all()
    context ={'machines': machines}
    return render(request,
        'computerapp/machine_list.html',
            context )

def machine_detail_view(request , pk ):
    machine = get_object_or_404(Machine , id=pk)
    context ={'machine': machine}
    return render(request ,
        'computerapp/machine_detail.html',
            context )






def personne_list_view(request) :
    personnes = Personne.objects.all()
    context ={'personnes': personnes}
    return render(request,
        'computerapp/personne_list.html',
            context )

def personne_detail_view(request , pk ):
    personne = get_object_or_404(Personne , id=pk)
    context ={'personne': personne}
    return render(request ,
        'computerapp/personne_detail.html',
            context )