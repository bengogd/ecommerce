from django.shortcuts import render, get_object_or_404
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from .models import Listing

#main view
def index(request):
    listings = Listing.objects.order_by('-list_date').filter(is_published=True) #get all published listings, ordered by newest first

    paginator = Paginator(listings, 6)
    page = request.GET.get('page')
    paged_listings = paginator.get_page(page)

    context = {
        'listings': paged_listings
    }

    return render(request, 'index.html', context)

#detail view
def listing(request, listing_id):
    listing = get_object_or_404(Listing, pk=listing_id) #Return 404 error if no object found
    other_images = []
    
    # iterate over photo_1 up to but not including photo_7 (doesn't exist)
    # append the url, only if it exists on the object. We get a ValueError
    # if it doesn't. The try/except block helps us mitigate this while
    # still throwing errors for other unexpected problems.
    for n in range(1, 7):
        try:
            other_images.append(getattr(listing, f'photo_{n}').url)
        except ValueError:
            continue

    # We should now have a list with a variable length of 1-6 to pass 
    # onto the Django template. Pass it along with the listing in the 
    # context.
    context = {
        'listing': listing,
        'other_images': other_images
    }
    return render(request, 'detail.html', context=context)

