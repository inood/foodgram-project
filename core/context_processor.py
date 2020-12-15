from core.models.cart import Cart


def get_cart_count(request):
    if request.user.is_authenticated:
        cart_count = Cart.objects.filter(
            user=request.user
        ).count()
    else:
        cart_count = None
    return {'cart_count': cart_count}
