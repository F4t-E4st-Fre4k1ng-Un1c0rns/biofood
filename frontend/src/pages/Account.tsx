import { load } from "@/api/orders";
import Button from "@/components/Button";
import DishInCart from "@/components/DishInCart";
import Error from "@/components/Error";
import LoadingIcon from "@/components/LoadingIcon";
import OrderStatus from "@/components/OrderStatus";
import { useAuthStore } from "@/store/auth";
import LoadingState from "@/types/LoadingState";
import Order from "@/types/Order";
import { uuidToOrderNumber } from "@/utils/uuidToOrderNumber";
import { useEffect, useState } from "react";
import { Link, useNavigate } from "react-router";

function Account() {
  const navigate = useNavigate();
  const auth = useAuthStore();

  const [orders, setOrders] = useState<Order[] | undefined>();
  const [ordersState, setOrdersState] = useState(LoadingState.loading);

  useEffect(() => {
    if (!auth.loggedIn) {
      return;
    }

    load()
      .then((orders) => {
        setOrders(orders);
        setOrdersState(LoadingState.ok);
      })
      .catch(() => setOrdersState(LoadingState.error));
  }, []);

  if (!auth.loggedIn) {
    navigate("/login", { replace: true });
  }
  return (
    <div className="flex flex-col gap-8">
      <h1>Аккаунт</h1>
      <p>{auth.user?.email}</p>
      <Button className="w-full" color="primary" onClick={auth.logout}>
        Выйти
      </Button>

      {auth.user?.role === "staff" && (
        <>
          <Link className="block w-full" to="/pos/chef">
            <Button className="w-full" color="accent">
              Панель повара
            </Button>
          </Link>
          <Link className="block w-full" to="/account/qr/">
            <Button className="w-full" color="accent">
              QR для входа в панель повора
            </Button>
          </Link>
        </>
      )}

      <h1>История заказов</h1>
      {ordersState === LoadingState.loading && <LoadingIcon />}
      {ordersState === LoadingState.error && <Error code={500} />}
      {ordersState === LoadingState.ok &&
        orders?.map((order) => {
          return (
            <div key={order.id}>
              <h2 className="mb-4">
                Заказ №{uuidToOrderNumber(order.id)}
                {order.takeoutTime && (
                  <> к {order.takeoutTime.toLocaleString("ru-RU")}</>
                )}{" "}
                <OrderStatus status={order.status} />
              </h2>

              {order?.items?.map((item) => {
                return (
                  <DishInCart
                    count={item.amount}
                    dish={item.dish}
                    key={item.dish.id}
                    showChangeButton={false}
                    showImage
                    showPrice
                  />
                );
              })}
            </div>
          );
        })}
    </div>
  );
}

export default Account;
