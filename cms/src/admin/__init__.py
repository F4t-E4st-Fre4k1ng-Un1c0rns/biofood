from .auth import AdminAuth

from .models.user import UserAdmin
from .models.dish import DishAdmin
from .models.category import CategoryAdmin
from .models.order import OrderAdmin
from .models.order_item import OrderItemAdmin
from .models.shopping_cart_item import ShoppingCartItemAdmin

authentication_backend = AdminAuth(secret_key="...")
models = [
    UserAdmin,
    DishAdmin,
    CategoryAdmin,
    OrderAdmin,
    OrderItemAdmin,
    ShoppingCartItemAdmin
]
