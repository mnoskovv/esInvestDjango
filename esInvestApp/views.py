from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Deal
from .forms import DealForm
import requests
from django.contrib import messages

# Create your views here.
class privatBankCurrencyCourse:
    @staticmethod
    def get():
        url = 'https://api.privatbank.ua/p24api/pubinfo?json&exchange&coursid=5'
        data = requests.get(url).json()
        currency_course = {
            'usd': data[0]['sale'],
            'eur': data[1]['sale'],
        }
        return currency_course

def index(request):
    deals = Deal.objects.all().order_by('-create_date')[:5]

    context = {
        'deals' : deals,
    }
    return render(request, 'esInvestApp/index.html', context)


def profile(request):
    currency_course = privatBankCurrencyCourse.get()
    deals = Deal.objects.filter(owner = request.user)

    open_deals = [d for d in deals if d.open_state == True]
    closed_deals = [d for d in deals if d.open_state == False]
    context = {
        'usd': currency_course["usd"],
        'eur': currency_course["eur"],
        'balance': request.user.profile.balance,
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
            if request.user.profile.balance >= deal.summary:
                request.user.profile.balance -= deal.summary
                request.user.save()
                deal.save()
                messages.success(request, 'Cделка успешно заключена!')
            else:
                messages.error(request, 'Недостаточно средств на счету!')


    return HttpResponseRedirect(reverse('esInvestApp:profile'))

def start(request):
    form = DealForm()

    context = {
        'form':form,
    }
    return render(request, 'esInvestApp/start.html',context)
