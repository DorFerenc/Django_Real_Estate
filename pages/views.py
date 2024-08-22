from django.shortcuts import render
from django.http import HttpResponse

from listings.models import Listing
from realtors.models import Realtor

# Create your views here.
def index(request):
    # return HttpResponse('<h1>Hello World</h1>')
    listings_from_db = Listing.objects.order_by('-list_date').filter(is_published=True)[:3]

    context = {
        'listings': listings_from_db
    }

    return render(request, 'pages/index.html', context)

def about(request):
    # Get all realtors
    realtors_from_db = Realtor.objects.order_by('-hire_date')
    # Get mvp
    mvp_realtors_from_db = Realtor.objects.all().filter(is_mvp=True)

    context = {
        'realtors': realtors_from_db,
        'mvp_realtors': mvp_realtors_from_db
    }
    return render(request, 'pages/about.html', context)