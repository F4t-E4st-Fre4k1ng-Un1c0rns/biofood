import Button from "@/components/Button";
import LoadingIcon from "@/components/LoadingIcon";
import PosOrder from "@/components/PosOrder";
import { useAuthStore } from "@/store/auth";
import { useCacheStore } from "@/store/cache";
import LoadingState from "@/types/LoadingState";
import Order from "@/types/Order";
import OrderStatus from "@/types/OrderStatus";
import { useEffect, useState } from "react";
import { Navigate, useNavigate } from "react-router";

function ChefKanban() {
  const auth = useAuthStore();
  const cache = useCacheStore();
  const navigate = useNavigate();
  const [state, setState] = useState(LoadingState.loading);

  const [pendingOrders, setPendingOrders] = useState<Order[]>([]);
  const [acceptedOrders, setAcceptedOrders] = useState<Order[]>([]);
  const [cookingOrders, setCookingOrders] = useState<Order[]>([]);
  const [readyOrders, setReadyOrders] = useState<Order[]>([]);

  useEffect(() => {
    setState(LoadingState.loading);
    setPendingOrders(
      Object.entries(cache.orders)
        .map(([, order]) => order)
        .filter((order) => order.status === OrderStatus.pending)
    );
    setAcceptedOrders(
      Object.entries(cache.orders)
        .map(([, order]) => order)
        .filter((order) => order.status === OrderStatus.accepted)
    );
    setCookingOrders(
      Object.entries(cache.orders)
        .map(([, order]) => order)
        .filter((order) => order.status === OrderStatus.cooking)
    );
    setReadyOrders(
      Object.entries(cache.orders)
        .map(([, order]) => order)
        .filter((order) => order.status === OrderStatus.ready)
    );
    setState(LoadingState.ok);
  }, [cache.orders]);

  const checkLogout = () => {
    if (confirm("Вы точно хотите выйти?")) {
      auth.logout();
      navigate("/pos/login");
    }
  };

  if (auth.user?.role !== "staff") {
    return <Navigate to="/pos/login" />;
  }

  return (
    <>
      <header className="flex justify-between p-4">
        <div>
          {state === LoadingState.loading && <LoadingIcon />}
          {state === LoadingState.error && <span>Ошибка!</span>}
        </div>
        <div>
          <Button color="primary" onClick={checkLogout}>
            Выйти
          </Button>
        </div>
      </header>
      <div className="grid grid-cols-3 m-4 gap-8">
        <div>
          <h1>Ожидают готовки</h1>
          {pendingOrders.map((order) => (
            <PosOrder key={order.id} order={order} />
          ))}
          {acceptedOrders.map((order) => (
            <PosOrder key={order.id} order={order} />
          ))}
        </div>
        <div>
          <h1>Готовятся</h1>
          {cookingOrders.map((order) => (
            <PosOrder key={order.id} order={order} />
          ))}
        </div>
        <div>
          <h1>Ожидают выдачи</h1>
          {readyOrders.map((order) => (
            <PosOrder key={order.id} order={order} />
          ))}
        </div>
      </div>
    </>
  );
}
export default ChefKanban;
