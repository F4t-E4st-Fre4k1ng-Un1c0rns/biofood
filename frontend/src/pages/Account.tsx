import Button from "@/components/Button";
import DishInCart from "@/components/DishInCart";
import OrderStatus from "@/components/OrderStatus";
import { useAuthStore } from "@/store/auth";
import { useCacheStore } from "@/store/cache";
import { uuidToOrderNumber } from "@/utils/uuidToOrderNumber";
import { useMemo } from "react";
import { Link, useNavigate } from "react-router";

function Account() {
  const navigate = useNavigate();
  const auth = useAuthStore();
  const cache = useCacheStore();

  const orders = useMemo(() => {
    return Object.entries(cache.orders)
      .map(([, order]) => order)
      .reverse();
  }, [cache.orders]);

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
          <a className="block w-full" href="/src/pos/index.html#/chef">
            <Button className="w-full" color="accent">
              Панель повара
            </Button>
          </a>
          <Link className="block w-full" to="/account/qr/">
            <Button className="w-full" color="accent">
              QR для входа в панель повора
            </Button>
          </Link>
        </>
      )}

      <h1>История заказов</h1>
      {orders.map((order) => {
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
