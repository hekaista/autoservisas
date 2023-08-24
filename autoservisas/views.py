from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from .models import Modelis, Automobilis, Uzsakymas, Paslauga


# Create your views here.

def index(request):
    num_modeliai = Modelis.objects.all().count()
    num_automobiliai = Automobilis.objects.all().count()
    num_uzsakymai = Uzsakymas.objects.all().count()
    num_uzsakymai_l = Uzsakymas.objects.filter(status__exact='L').count()
    num_paslaugos = Paslauga.objects.all().count()

    context_t = {
        'num_modeliai_t': num_modeliai,
        'num_automobiliai_t': num_automobiliai,
        'num_uzsakymai_t': num_uzsakymai,
        'num_uzsakymai_onhold_t': num_uzsakymai_l,
        'num_paslaugos_t': num_paslaugos,
    }

    return render(request, 'index.html', context=context_t)


def automods(request):
    automods = Modelis.objects.all()
    context_t = {
        'automods_t': automods
    }
    return render(request, 'automods.html', context=context_t)


def auto_detail(request, id):
    automod = get_object_or_404(Modelis, pk=id)
    automobiliai = automod.automobiliai.all()
    context = {
        'automod': automod,
        'automobiliai': automobiliai
    }
    return render(request, 'auto_detail.html', context=context)
