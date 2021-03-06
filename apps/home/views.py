from apps.visacard.views import get_visacard
from apps.news.views import get_news
from apps.visacard.views import get_visacard
from django.shortcuts import render
from apps.coins.views import get_coins
from apps.coins.views import get_featured_coins
from django.template.loader import render_to_string
from django.core.mail import send_mail
from django.utils.html import strip_tags


# Create your views here.
def home(request):
    context = {
        'coins' : get_coins(),
        'news'  : get_news(),
        'featured_coins' : get_featured_coins()
    }
    return render(request, 'pages/index.html', context)

def subscribe(request):
    subscribe_name = request.POST.get('subscribeName')
    subscribe_number = request.POST.get('subscribeNumber')
    subscribe_email = request.POST.get('subscribeEmail')
    subscribe_message = request.POST.get('subscribeMessage')

    context = {
        'subscribe_name' : subscribe_name,
        'subscribe_number' : subscribe_number,
        'subscribe_email' : subscribe_email,
        'subscribe_message' : subscribe_message
    }
    
    email_template_html = render_to_string('emails/subscribe.html', context)
    email_template_txt = strip_tags(email_template_html)

    subject = 'Subscription Email | cryptobit'
    from_email = 'subscribe@cryptobit.com'
    to_email = ['tawassul02@gmail.com']
    send_mail(
        subject=subject,
        from_email=from_email, 
        recipient_list = to_email, 
        html_message=email_template_html, 
        message=email_template_txt
        )

    return render(request, 'emails/thankyou.html')    


def trade(request):
    return render(request, 'pages/express.html')


def market(request):
    context = {
        'coins' : get_coins(),
    }
    return render(request, 'pages/market.html', context)


def visacard(request):
    context = {
        'visacard' : get_visacard()
    }
    return render(request, 'pages/visacard.html', context)


def forgotpassword(request):
    return render(request, 'pages/forgotpassword.html')


def register(request):
    return render(request, 'pages/register.html')


def login(request):
    return render(request, 'pages/login.html')



def coinDisplay(request):
    context = {
        'coins' : get_coins(),
    }

    return render(request, 'pages/coinDisplay.html', context)



def details(request):
    context = {
        'coins' : get_coins(),
    }
    return render(request, 'pages/details.html', context)

  