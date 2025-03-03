import { put } from "@/api/orders";
import DishInCart from "@/components/DishInCart";
import Error from "@/components/Error";
import LoadingIcon from "@/components/LoadingIcon";
import { useCartStore } from "@/store/cart";
import LoadingState from "@/types/LoadingState";
import Order from "@/types/Order";
import { useEffect, useState } from "react";
import { useSearchParams } from "react-router";

export default () => {
  const cart = useCartStore();
  const [state, setState] = useState(LoadingState.loading);
  const [params, setParams] = useSearchParams();
  const [order, setOrder] = useState<Order | undefined>();

  useEffect(() => {
    if (!params.get("done")) {
      cart.clearCart();
      put(params.get("takeoutTime") ?? "").then((order) => {
        setState(LoadingState.ok);
        setOrder(order);
      });
      setParams("done=1");
    } else {
      setState(LoadingState.error);
    }
  }, []);
  return (
    <div className="flex flex-col gap-8">
      <h1>Спасибо за заказ!</h1>
      {state == LoadingState.loading && <LoadingIcon />}
      {state == LoadingState.ok && order && (
        <>
          <h2>Ваш заказ:</h2>
          <p>Будет готов к {order.takeoutTime.toLocaleDateString("ru-RU")}</p>
          {order.items.map((item) => {
            return (
              <DishInCart
                dish={item.dish}
                count={item.amount}
                showChangeButton={false}
                showPrice={true}
              />
            );
          })}
        </>
      )}
      {state == LoadingState.error && <Error code={500} />}
    </div>
  );
};
