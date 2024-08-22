from django.shortcuts import render, get_object_or_404

# Create your views here.
from .models import Listing
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

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
    return render(request, 'listings/search.html')