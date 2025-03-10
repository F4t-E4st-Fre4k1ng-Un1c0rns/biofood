import { useAuthStore } from "@/store/auth";
import Order from "@/types/Order";

type ApiOrder = Order & { takeoutTime: string | null };

export async function load(
  status: Order["status"]
): Promise<Order[] | undefined> {
  const { getState: getAuthState } = useAuthStore;
  if (!getAuthState().loggedIn) {
    return;
  }

  const params = new URLSearchParams({
    status,
  });

  const response = await fetch(
    `${import.meta.env.VITE_API_BASE_URL}/orders/today?${params}`,
    {
      method: "GET",
      headers: {
        Authorization: `Bearer ${getAuthState().user?.token}`,
      },
    }
  );
  const json = await response.json();

  const orders = json.items;
  return orders.map((order: ApiOrder) => ({
    ...order,
    takeoutTime: order.takeoutTime ? new Date(order.takeoutTime) : null,
  }));
}

export async function patch(
  id: Order["id"],
  status: Order["status"]
): Promise<Order[] | undefined> {
  const { getState: getAuthState } = useAuthStore;
  if (!getAuthState().loggedIn) {
    return;
  }
  await fetch(`${import.meta.env.VITE_API_BASE_URL}/orders/${id}`, {
    method: "PATCH",
    headers: {
      Authorization: `Bearer ${getAuthState().user?.token}`,
      "Content-Type": "application/json",
    },
    body: JSON.stringify({ status }),
  });
}
