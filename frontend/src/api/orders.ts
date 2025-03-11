import { useAuthStore } from "@/store/auth";
import Order from "@/types/Order";

export async function put(
  takeoutTime: string | null
): Promise<Order | undefined> {
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
  const order = await response.json();

  order.takeoutTime = order.takeoutTime ? new Date(order.takeoutTime) : null;
  return order;
}
