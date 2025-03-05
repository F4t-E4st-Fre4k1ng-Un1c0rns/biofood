import { put } from "@/api/orders";
import DishInCart from "@/components/DishInCart";
import Error from "@/components/Error";
import LoadingIcon from "@/components/LoadingIcon";
import OrderStatus from "@/components/OrderStatus";
import { useCacheStore } from "@/store/cache";
import LoadingState from "@/types/LoadingState";
import Order from "@/types/Order";
import { useEffect, useState } from "react";
import { useParams, useSearchParams } from "react-router";

export default () => {
  const cache = useCacheStore();
  const [state, setState] = useState(LoadingState.loading);
  const [params] = useSearchParams();
  const { id } = useParams() as { id: Order["id"] };
  const [order, setOrder] = useState<Order | undefined>();

  useEffect(() => {
    console.log(cache.orders);
    if (cache.orders[id]) {
      setOrder(cache.orders[id]);
      setState(LoadingState.ok);
    } else {
      cache.fetchOrder(id).catch(() => setState(LoadingState.error));
    }
  }, [cache.orders[id]]);
  return (
    <div className="flex flex-col gap-8">
      <h1>{params.get("new") ? "Спасибо за заказ!" : "Заказ"}</h1>
      {state == LoadingState.loading && <LoadingIcon />}
      {state == LoadingState.ok && order && (
        <>
          <h2>Ваш заказ:</h2>
          <p>Будет готов к {order.takeoutTime.toLocaleDateString("ru-RU")}</p>
          <OrderStatus status={order.status} />
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
