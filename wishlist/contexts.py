from django.conf import settings

def wishlist_contents(request):

    wishlist_items = []
    total = 0
    product_count = 0
    
    context = {
        'wishlist_items': wishlist_items,
        'total': total,
        'product_count': product_count,
        
    }

    return context