from django.shortcuts import render, redirect, reverse, HttpResponse, get_object_or_404
from django.contrib import messages

from products.models import Product

def view_wishlist(request):
    """ A view that renders the wishlist contents page """

    wishlist = request.session.get('wishlist', {})
    print(wishlist)

    return render(request, 'wishlist/wishlist.html')

def add_to_wishlist(request, item_id):
    """ Add a quantity of the specified product to the wishlist """
    product = get_object_or_404(Product, pk=item_id)
    quantity_str = request.POST.get('quantity')
    if quantity_str is not None:
        quantity = int(quantity_str)
    else:
        quantity = 1  # Default quantity if not provided
    redirect_url = request.POST.get('redirect_url', reverse('view_wishlist'))
    size = request.POST.get('product_size')
    wishlist = request.session.get('wishlist', {})

    if size:
        wishlist.setdefault(item_id, {'items_by_size': {}})
        wishlist[item_id]['items_by_size'].setdefault(size, 0)
        wishlist[item_id]['items_by_size'][size] += quantity
        messages.success(request, f'Added size {size.upper()} {product.name} to your wishlist')
    else:
        wishlist[item_id] = wishlist.get(item_id, 0) + quantity
        messages.success(request, f'Added {product.name} to your wishlist')

    request.session['wishlist'] = wishlist
    return redirect(redirect_url)
    

def adjust_wishlist(request, item_id):
    """Adjust the quantity of the specified product in the wishlist"""
    product = get_object_or_404(Product, pk=item_id)
    quantity_str = request.POST.get('quantity')
    if quantity_str is not None:
        quantity = int(quantity_str)
    else:
        quantity = 0  # Default quantity if not provided
    size = request.POST.get('product_size')
    wishlist = request.session.get('wishlist', {})

    if size:
        if quantity > 0:
            wishlist[item_id]['items_by_size'][size] = quantity
            messages.success(request, f'Updated size {size.upper()} {product.name} quantity to {quantity}')
        else:
            del wishlist[item_id]['items_by_size'][size]
            if not wishlist[item_id]['items_by_size']:
                wishlist.pop(item_id)
            messages.success(request, f'Removed size {size.upper()} {product.name} from your wishlist')
    else:
        if quantity > 0:
            wishlist[item_id] = quantity
            messages.success(request, f'Updated {product.name} quantity to {quantity}')
        elif quantity == 0:
            wishlist.pop(item_id, None)  # Remove the item if quantity is 0
            messages.success(request, f'Removed {product.name} from your wishlist')

    request.session['wishlist'] = wishlist
    return redirect(reverse('view_wishlist'))

def remove_from_wishlist(request, item_id):
    """Remove the item from the wishlist"""
    try:
        product = get_object_or_404(Product, pk=item_id)
        size = request.POST.get('product_size')
        wishlist = request.session.get('wishlist', {})

        if size:
            if wishlist.get(item_id) and wishlist[item_id]['items_by_size'].get(size):
                del wishlist[item_id]['items_by_size'][size]
                if not wishlist[item_id]['items_by_size']:
                    wishlist.pop(item_id)
                messages.success(request, f'Removed size {size.upper()} {product.name} from your wishlist')
        elif item_id in wishlist:
            del wishlist[item_id]
            messages.success(request, f'Removed {product.name} from your wishlist')

        request.session['wishlist'] = wishlist
        return HttpResponse(status=200)

    except Exception as e:
        messages.error(request, f'Error removing item: {e}')
        return HttpResponse(status=500)
        
'''wednesday evening atttempt 
def view_wishlist(request):
    """ A view that renders the wishlist contents page """
    return render(request, 'wishlist/wishlist.html')

def add_to_wishlist(request, item_id):
    """ Add a quantity of the specified product to the shopping wishlist """
    product = get_object_or_404(Product, pk=item_id)
    quantity_str = request.POST.get('quantity')
    if quantity_str is not None:
        quantity = int(quantity_str)
    else:
        quantity = 1  # Default quantity if not provided
    redirect_url = request.POST.get('redirect_url', reverse('view_wishlist'))
    size = request.POST.get('product_size')
    wishlist = request.session.get('wishlist', {})

    if size:
        if item_id in wishlist:
            if size in wishlist[item_id].get('items_by_size', {}):
                wishlist[item_id]['items_by_size'][size] += quantity
                messages.success(request, f'Updated size {size.upper()} {product.name} quantity to {wishlist[item_id]["items_by_size"][size]}')
            else:
                wishlist[item_id].setdefault('items_by_size', {})[size] = quantity
                messages.success(request, f'Added size {size.upper()} {product.name} to your wishlist')
        else:
            wishlist[item_id] = {'items_by_size': {size: quantity}}
            messages.success(request, f'Added size {size.upper()} {product.name} to your wishlist')
    else:
        if item_id in wishlist:
            wishlist[item_id] += quantity
            messages.success(request, f'Updated {product.name} quantity to {wishlist[item_id]}')
        else:
            wishlist[item_id] = quantity
            messages.success(request, f'Added {product.name} to your wishlist')

    request.session['wishlist'] = wishlist
    return redirect(redirect_url)

def adjust_wishlist(request, item_id):
    """Adjust the quantity of the specified product to the specified amount"""
    product = get_object_or_404(Product, pk=item_id)
    quantity_str = request.POST.get('quantity')
    if quantity_str is not None:
        quantity = int(quantity_str)
    else:
        quantity = 0  # Default quantity if not provided
    size = request.POST.get('product_size')
    wishlist = request.session.get('wishlist', {})

    if size:
        # Ensure the item has a dictionary structure for sizes
        if isinstance(wishlist.get(item_id), int):
            # If the item is stored as an int, convert it to a size dictionary
            wishlist[item_id] = {'items_by_size': {}}
        if 'items_by_size' not in wishlist[item_id]:
            wishlist[item_id]['items_by_size'] = {}

        if quantity > 0:
            wishlist[item_id]['items_by_size'][size] = quantity
            messages.success(request, f'Updated size {size.upper()} {product.name} quantity to {quantity}')
        else:
            del wishlist[item_id]['items_by_size'][size]
            if not wishlist[item_id]['items_by_size']:
                wishlist.pop(item_id)
            messages.success(request, f'Removed size {size.upper()} {product.name} from your wishlist')
    else:
        # Ensure the item does not have a size dictionary
        if isinstance(wishlist.get(item_id), dict) and 'items_by_size' in wishlist[item_id]:
            # If the item is stored with sizes, sum all sizes into a single quantity
            total_quantity = sum(wishlist[item_id]['items_by_size'].values())
            wishlist[item_id] = total_quantity

        if quantity > 0:
            wishlist[item_id] = quantity
            messages.success(request, f'Updated {product.name} quantity to {quantity}')
        else:
            wishlist.pop(item_id)
            messages.success(request, f'Removed {product.name} from your wishlist')

    request.session['wishlist'] = wishlist
    return redirect(reverse('view_wishlist'))

def remove_from_wishlist(request, item_id):
    """Remove the item from the wishlist"""
    try:
        product = get_object_or_404(Product, pk=item_id)
        size = request.POST.get('product_size')
        wishlist = request.session.get('wishlist', {})

        if size:
            if item_id in wishlist and 'items_by_size' in wishlist[item_id]:
                if size in wishlist[item_id]['items_by_size']:
                    del wishlist[item_id]['items_by_size'][size]
                    if not wishlist[item_id]['items_by_size']:
                        del wishlist[item_id]
                    messages.success(request, f'Removed size {size.upper()} {product.name} from your wishlist')
        else:
            if item_id in wishlist:
                del wishlist[item_id]
                messages.success(request, f'Removed {product.name} from your wishlist')

        request.session['wishlist'] = wishlist
        return HttpResponse(status=200)

    except Exception as e:
        messages.error(request, f'Error removing item: {e}')
        return HttpResponse(status=500)'''
