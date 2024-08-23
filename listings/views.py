from django.shortcuts import render, get_object_or_404

# Create your views here.
from .models import Listing
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from .choices import price_choices, bedroom_choices, state_choices


def index(request):
    # listings_from_db = Listing.objects.all()
    listings_from_db = Listing.objects.order_by('-list_date').filter(is_published=True) # order listings by date

    paginator = Paginator(listings_from_db, 3)
    page = request.GET.get('page')
    paged_listings = paginator.get_page(page)
    
    context = {
        'listings': paged_listings
    }

    return render(request, 'listings/listings.html', context)

def listing(request, listing_id):
    listing_from_db = get_object_or_404(Listing, pk=listing_id)

    context = {
        'listing': listing_from_db
    }

    return render(request, 'listings/listing.html', context)

def search(request):
    queryset_list = Listing.objects.order_by('-list_date')
    
    # Keywords
    if 'keywords' in request.GET:
        keywords = request.GET['keywords']
        if keywords:
            queryset_list = queryset_list.filter(description__icontains=keywords)  
    
    # City
    if 'city' in request.GET:
        city = request.GET['city']
        if city:
            queryset_list = queryset_list.filter(city__iexact=city)
    
    # State
    if 'state' in request.GET:
        state = request.GET['state']
        if state:
            queryset_list = queryset_list.filter(state__iexact=state)
            
    # Bedrooms - up to the number of bedrooms 
    if 'bedrooms' in request.GET:
        bedrooms = request.GET['bedrooms']
        if bedrooms:
            queryset_list = queryset_list.filter(bedrooms__lte=bedrooms)
            
    # # Price - up to the price given 
    if 'price' in request.GET:
        price = request.GET['price']
        if price:
            print(price)
            if price == str(1000000):
                queryset_list = queryset_list.filter(price__gte=price)
            else:
                queryset_list = queryset_list.filter(price__lte=price) 
    
    context = {
        'state_choices': state_choices,
        'bedroom_choices': bedroom_choices,
        'price_choices': price_choices,
        'listings': queryset_list,
        'values': request.GET
    }
        
    return render(request, 'listings/search.html', context)