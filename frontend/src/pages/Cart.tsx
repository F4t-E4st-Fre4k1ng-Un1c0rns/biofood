import Button from "@/components/Button";
import DishInCart from "@/components/DishInCart";
import { useAuthStore } from "@/store/auth";
import { useCartStore } from "@/store/cart";
import { useCacheStore } from "@/store/cache";
import { Fragment, useMemo, useState } from "react";
import { useNavigate } from "react-router";
import LoadingState from "@/types/LoadingState";
import LoadingIcon from "@/components/LoadingIcon";
import { put } from "@/api/orders";

function Cart() {
  const navigate = useNavigate();
  const cache = useCacheStore();
  const cart = useCartStore();
  const auth = useAuthStore();
  const [state, setState] = useState(LoadingState.ok);

  const now = new Date();
  const nowString = `${now.getHours()}:${now.getMinutes()}`;
  const [timeValue, setTimeValue] = useState<string | undefined>();
  const cookBy = useMemo(() => {
    if (!timeValue) {
      return;
    }
    const hours = parseInt(timeValue.slice(0, 2));
    const minutes = parseInt(timeValue.slice(3));
    const to = now;
    to.setHours(hours);
    to.setMinutes(minutes);
    return to;
  }, [timeValue]);

  const sum = useMemo(() => {
    let sum = 0;
    for (const item of Object.entries(cart.cart)) {
      if (item[0] in cache.dishes) {
        sum += cache.dishes[item[0]].price * item[1];
      }
    }

    return sum;
  }, [cache.dishes, cart.cart]);

  const confirmOrder = () => {
    if (!auth.loggedIn) {
      navigate("/login");
      return;
    }
    setState(LoadingState.loading);
    cart.clearCart();
    put(cookBy?.toISOString() ?? null)
      .then((order) => {
        if (!order || !order.id) {
          navigate(`/order/500?new=1`);
          return;
        }
        cache.setCachedOrders([order]);
        navigate(`/order/${order.id}?new=1`);
      })
      .catch((event) => {
        console.error(event);
        navigate("/order/500?new=1");
      });
  };

  return (
    <>
      <div>
        <h1 className="pb-8">Корзина</h1>
        {Object.entries(cart.cart).map(([dishId, count]) => {
          if (!count) {
            return;
          }
          if (!(dishId in cache.dishes)) {
            return <Fragment key={dishId} />;
          }
          const add = () => {
            cart.addToCart(dishId);
          };
          const remove = () => {
            cart.removeFromCart(dishId);
          };
          return (
            <DishInCart
              add={add}
              count={count}
              dish={cache.dishes[dishId]}
              key={dishId}
              remove={remove}
              showChangeButton
              showImage
              showPrice
            />
          );
        })}
      </div>
      <div>
        <div className="flex justify-between py-8">
          <h2>Приготовить к</h2>
          <input
            max="18:00"
            min={nowString}
            onChange={(event) => setTimeValue(event.target.value)}
            type="time"
          />
        </div>
        {Object.keys(cart.cart).length ? (
          <>
            {state === LoadingState.ok && (
              <Button className="w-full" color="primary" onClick={confirmOrder}>
                {`Заказать за ${sum.toLocaleString("ru-RU")} ₽`}
              </Button>
            )}
            {state === LoadingState.loading && <LoadingIcon />}
          </>
        ) : (
          <h2>⚠️ Сначала добавьте продукты в корзину</h2>
        )}
      </div>
    </>
  );
}

export default Cart;
