from .models import Cart, User


def cart_item(request):
    cart_items = []
    cart = {}

    if request.user.is_authenticated:
        user = request.user
        user = User.objects.get(username=user)
        cart, created = Cart.objects.get_or_create(user=user)
        cart_items = cart.cartitem_set.all()

    return {'cart_items': cart_items, 'cart': cart}
