import { useAuthStore } from "@/store/auth";
import { useCacheStore } from "@/store/cache";
import { SSE } from "sse.js";

function sseSubscribeOrders(all?: boolean) {
  const { getState: getCachedState, setState: setCacheState } = useCacheStore;
  const { getState: getAuthState } = useAuthStore;
  const eventSource = new SSE(
    `${import.meta.env.VITE_API_BASE_URL}/orders${all ? "/all" : ""}`,
    {
      method: "GET",
      headers: {
        Authorization: `Bearer ${getAuthState().user?.token}`,
      },
    }
  );
  eventSource.onmessage = (event) => {
    const { items } = JSON.parse(event.data);
    for (const item of items) {
      setCacheState({
        ...getCachedState(),
        orders: {
          ...getCachedState().orders,
          [item.id]: item,
        },
      });
    }
  };
  eventSource.onerror = () => {
    sseSubscribeOrders(all);
  };
}

export default sseSubscribeOrders;
