from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.db.models import Q
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


def automobiliai(request):
    automobiliai = Automobilis.objects.all()
    context = {
        'automobiliai': automobiliai
    }
    return render(request, 'automobiliai.html', context=context)


def automobilis(request, auto_id):
    automobilis = get_object_or_404(Automobilis, pk=auto_id)
    context = {
        'automobilis': automobilis
    }
    return render(request, 'automobilis.html', context=context)


def paslaugos_list(request):
    paslaugos = Paslauga.objects.all()
    context = {
        'paslaugos_t': paslaugos
    }
    return render(request, 'paslaugos.html', context)


class UzsakymaiListView(generic.ListView):
    model = Uzsakymas
    context_object_name = 'uzsakymai'
    template_name = 'uzsakymai_list.html'


class UzsakymasDetailView(generic.DetailView):
    model = Uzsakymas
    context_object_name = 'uzsakymas'
    template_name = 'uzsakymas_detail.html'


def search(request):
    query = request.GET.get('search_text')
    search_results = Automobilis.objects.filter(
        Q(klientas__icontains=query) |
        Q(modelis__marke__icontains=query) |
        Q(valstybinis_nr__icontains=query) |
        Q(vin__icontains=query)
    )
    context = {
        'query_t': query,
        'search_results_t': search_results
    }
    return render(request, 'search.html', context=context)
