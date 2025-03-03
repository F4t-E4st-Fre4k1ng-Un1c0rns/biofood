import Button from "@/components/Button";
import DishInCart from "@/components/DishInCart";
import { useAuthStore } from "@/store/auth";
import { useCartStore } from "@/store/cart";
import { useCatalogueStore } from "@/store/catalogue";
import { Fragment, useMemo, useState } from "react";
import { useNavigate } from "react-router";

export default () => {
  const navigate = useNavigate();
  const catalogue = useCatalogueStore();
  const cart = useCartStore();
  const auth = useAuthStore();

  const now = new Date();
  const nowString = `${now.getHours()}:${now.getMinutes()}`;
  const [timeValue, setTimeValue] = useState(
    `${now.getHours()}:${now.getMinutes()}`
  );
  const cookBy = useMemo(() => {
    const hours = parseInt(timeValue.slice(0, 2));
    const minutes = parseInt(timeValue.slice(3));
    const to = now;
    to.setHours(hours);
    to.setMinutes(minutes);
    return to;
  }, [timeValue]);

  const sum = useMemo(() => {
    let sum = 0;
    for (let item of Object.entries(cart.cart)) {
      if (item[0] in catalogue.dishes) {
        sum += catalogue.dishes[item[0]].price * item[1];
      }
    }

    return sum;
  }, [catalogue.dishes, cart.cart]);

  const confirmOrder = () => {
    if (!auth.loggedIn) {
      navigate("/login");
      return;
    }
    const params = new URLSearchParams({
      takeoutTime: cookBy.toISOString(),
    });
    navigate(`/order-done?${params}`, { replace: true });
  };

  return (
    <>
      <div>
        <h1 className="pb-8">Корзина</h1>
        {Object.entries(cart.cart).map(([dishId, count]) => {
          if (!(dishId in catalogue.dishes)) {
            return <Fragment key={dishId}></Fragment>;
          }
          const add = () => {
            cart.addToCart(dishId);
          };
          const remove = () => {
            cart.removeFromCart(dishId);
          };
          return (
            <DishInCart
              dish={catalogue.dishes[dishId]}
              count={count}
              add={add}
              remove={remove}
              showChangeButton={true}
              showPrice={true}
              key={dishId}
            />
          );
        })}
      </div>
      <div>
        <div className="flex justify-between py-8">
          <h2>Приготовить к</h2>
          <input
            type="time"
            min={nowString}
            max="18:00"
            onChange={(e) => setTimeValue(e.target.value)}
          />
        </div>
        <Button color="primary" onClick={confirmOrder} className="w-full">
          {`Заказать за ${sum.toLocaleString("ru-RU")} ₽`}
        </Button>
      </div>
    </>
  );
};
