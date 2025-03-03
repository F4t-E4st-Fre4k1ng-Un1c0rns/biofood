import { useAuthStore } from "@/store/auth";
import Order from "@/types/Order";

type ApiOrder = Order & { takeoutTime: string };

export async function put(takeoutTime: string): Promise<Order | undefined> {
  if (import.meta.env.VITE_MOCK_API) {
    throw new Error();
  }
  const { getState: getAuthState } = useAuthStore;
  if (!getAuthState().loggedIn) {
    return;
  }

  const response = await fetch(`${import.meta.env.VITE_API_BASE_URL}/orders`, {
    method: "POST",
    headers: {
      Authorization: `Bearer ${getAuthState().user?.token}`,
      "Content-Type": "application/json",
    },
    body: JSON.stringify({
      takeoutTime: takeoutTime,
    }),
  });
  const json = await response.json();

  const order = json.items[0];
  order.takeoutTime = new Date(takeoutTime);
  return order;
}

export async function load(): Promise<Order[] | undefined> {
  if (import.meta.env.VITE_MOCK_API) {
    throw new Error();
  }
  const { getState: getAuthState } = useAuthStore;
  if (!getAuthState().loggedIn) {
    return;
  }

  const response = await fetch(`${import.meta.env.VITE_API_BASE_URL}/orders`, {
    method: "GET",
    headers: {
      Authorization: `Bearer ${getAuthState().user?.token}`,
    },
  });
  const json = await response.json();

  const orders = json.items;
  return orders.map((order: ApiOrder) => ({
    ...order,
    takeoutTime: new Date(order.takeoutTime),
  }));
}
