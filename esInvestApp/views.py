from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Deal
from .forms import DealForm
# Create your views here.
def index(request):
    deals = Deal.objects.all().order_by('-create_date')[:5]

    context = {
        'deals' : deals,
    }
    return render(request, 'esInvestApp/index.html', context)


def profile(request):
    form = DealForm()

    deals = Deal.objects.filter(owner = request.user)

    open_deals = [d for d in deals if d.open_state == True]
    closed_deals = [d for d in deals if d.open_state == False]
    context = {
        'form':form,
        'open_deals':open_deals,
        'closed_deals':closed_deals,
    }
    return render(request, 'esInvestApp/profile.html', context)

def open_deal(request):
    owner = request.user
    if request.method == 'POST':
        form  = DealForm(data=request.POST)

        if form.is_valid():
            deal = form.save(commit = False)
            deal.owner = owner
            deal.save()

    return HttpResponseRedirect(reverse('esInvestApp:profile'))

def start(request):
    form = DealForm()

    context = {
        'form':form,
    }
    return render(request, 'esInvestApp/start.html',context)
