import { useAuthStore } from "@/store/auth";
import Order from "@/types/Order";

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
