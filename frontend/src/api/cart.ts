import { useAuthStore } from "@/store/auth";
import Dish from "@/types/Dish";

interface DishInApiCart {
  amount: number;
  dish: Dish;
  id: string;
}

export async function load(): Promise<Record<Dish["id"], number>> {
  const { getState: getAuthState } = useAuthStore;
  if (!getAuthState().loggedIn) {
    return {};
  }

  const response = await fetch(
    `${import.meta.env.VITE_API_BASE_URL}/shopping-cart-items`,
    {
      method: "GET",
      headers: {
        Authorization: `Bearer ${getAuthState().user?.token}`,
      },
    }
  );
  const json = await response.json();
  const items: DishInApiCart[] = json.items;
  const dishes = items.map((item) => [item.dish.id, item.amount]);
  return Object.fromEntries(dishes);
}

export async function add(dishId: Dish["id"]): Promise<void> {
  if (import.meta.env.VITE_MOCK_API) {
    throw new Error();
  }

  const { getState: getAuthState } = useAuthStore;
  if (!getAuthState().loggedIn) {
    return;
  }

  await fetch(`${import.meta.env.VITE_API_BASE_URL}/shopping-cart-items`, {
    method: "PUT",
    body: JSON.stringify([
      {
        dishId,
        amount: 1,
      },
    ]),
    headers: {
      "Content-Type": "application/json",
      Authorization: `Bearer ${getAuthState().user?.token}`,
    },
  });
}

export async function remove(dishId: Dish["id"]): Promise<void> {
  if (import.meta.env.VITE_MOCK_API) {
    throw new Error();
  }

  const { getState: getAuthState } = useAuthStore;
  if (!getAuthState().loggedIn) {
    return;
  }

  await fetch(`${import.meta.env.VITE_API_BASE_URL}/shopping-cart-items`, {
    method: "DELETE",
    body: JSON.stringify([
      {
        dishId,
        amount: 1,
      },
    ]),
    headers: {
      "Content-Type": "application/json",
      Authorization: `Bearer ${getAuthState().user?.token}`,
    },
  });
}

export async function massAdd(cart: Record<Dish["id"], number>): Promise<void> {
  if (import.meta.env.VITE_MOCK_API) {
    throw new Error();
  }

  const { getState: getAuthState } = useAuthStore;
  if (!getAuthState().loggedIn) {
    return;
  }

  const backCart = Object.entries(cart).map((entry) => ({
    dishId: entry[0],
    amount: entry[1],
  }));

  await fetch(`${import.meta.env.VITE_API_BASE_URL}/shopping-cart-items`, {
    method: "PUT",
    body: JSON.stringify(backCart),
    headers: {
      "Content-Type": "application/json",
      Authorization: `Bearer ${getAuthState().user?.token}`,
    },
  });
}
