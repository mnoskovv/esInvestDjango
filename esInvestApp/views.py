from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Deal
from .forms import DealForm
import requests
from django.contrib import messages
from django.contrib.auth.decorators import login_required
import datetime
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.
class PrivatBankCurrencyCourse:
    
    currency_cache = {}

    @staticmethod
    def get():
        today = datetime.date.today()
        yesterday = today - datetime.timedelta(days=1)

        if today in PrivatBankCurrencyCourse.currency_cache:
            return PrivatBankCurrencyCourse.currency_cache[today]
        print("\t\tделаю хттп запрос")
        url = 'https://api.privatbank.ua/p24api/pubinfo?json&exchange&coursid=5'
        data = requests.get(url).json()
        if yesterday in PrivatBankCurrencyCourse.currency_cache:
            if PrivatBankCurrencyCourse.currency_cache[yesterday]['usd'] < data[0]['sale']:
                usd_state = "kurs_up"
            if PrivatBankCurrencyCourse.currency_cache[yesterday]['eur'] < data[1]['sale']:
                eur_state = "kurs_up"
        usd_state = "kurs_down"
        eur_state = "kurs_down"
        currency_course = {
            'date': today,
            'usd': data[0]['sale'],
            'usd_state': usd_state,
            'eur': data[1]['sale'],
            'eur_state': eur_state,
        }
        PrivatBankCurrencyCourse.currency_cache[today] = currency_course
        return currency_course

def index(request):
    deals = Deal.objects.all().order_by('-create_date')[:5]

    context = {
        'deals' : deals,
    }
    return render(request, 'esInvestApp/index.html', context)


@login_required
def profile(request):
    currency_course = PrivatBankCurrencyCourse.get()
    deals = Deal.objects.filter(owner = request.user)

    open_deals = [d for d in deals if d.open_state == True]
    closed_deals = [d for d in deals if d.open_state == False]

    paginator = Paginator(open_deals, 5)
    page = request.GET.get('page')
    try:
        open_deals = paginator.page(page)

    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        open_deals = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        open_deals = paginator.page(paginator.num_pages)

    paginator = Paginator(closed_deals, 5)
    page = request.GET.get('page2')
    try:
        closed_deals = paginator.page(page)

    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        closed_deals = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        closed_deals = paginator.page(paginator.num_pages)

    context = {
        'usd': currency_course["usd"],
        'eur': currency_course["eur"],
        'usd_state': currency_course["usd_state"],
        'eur_state': currency_course["eur_state"],
        'balance': request.user.profile.balance,
        'open_deals':open_deals,
        'closed_deals':closed_deals,
    }

    return render(request, 'esInvestApp/profile.html', context)

@login_required
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

@login_required
def start(request):
    form = DealForm()

    context = {
        'form':form,
    }
    return render(request, 'esInvestApp/start.html',context)
