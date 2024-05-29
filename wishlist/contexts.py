from django.conf import settings
from django.shortcuts import get_object_or_404
from products.models import Product

def wishlist_contents(request):

    wishlist_items = []
    total = 0
    product_count = 0

    wishlist = request.session.get('wishlist', {})

    for item_id, item_data in wishlist.items():
        product = get_object_or_404(Product, pk=item_id)
        if isinstance(item_data, dict) and 'items_by_size' in item_data:
            for size, quantity in item_data['items_by_size'].items():
                total += quantity * product.price
                product_count += quantity
                wishlist_items.append({
                    'product': product,
                    'quantity': quantity,
                    'size': size,
                })
        else:
            quantity = item_data if isinstance(item_data, int) else 0
            total += quantity * product.price
            product_count += quantity
            wishlist_items.append({
                'product': product,
                'quantity': quantity,
                'size': None,
            })
    
    context = {
        'wishlist_items': wishlist_items,
        'total': total,
        'product_count': product_count,
        
    }

    return context