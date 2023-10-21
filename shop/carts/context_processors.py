from .models import Cart, User


def cart_item(request):
    cart_items = []
    cart = {}

    if request.user.is_authenticated:
        username = request.user.username
        user = User.objects.get(username=username)
        cart, created = Cart.objects.get_or_create(username=user)
        cart_items = cart.cartitem_set.all()

    return {'cart_items': cart_items, 'cart': cart}
