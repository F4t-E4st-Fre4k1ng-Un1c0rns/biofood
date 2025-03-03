import { add, load, massAdd, remove } from "@/api/cart";
import Dish from "@/types/Dish";
import { create } from "zustand";

type IdType = Dish["id"];

export interface CartStore {
  cart: Record<IdType, number>;
  addToCart: (id: IdType) => void;
  removeFromCart: (id: IdType) => void;

  fetch: () => void;
  restoreCart: () => void;
  clearCart: () => void;
}

export const useCartStore = create<CartStore>((set) => ({
  cart: {},
  addToCart: (id: IdType) =>
    set((state) => {
      let count = 0;
      add(id);
      if (state.cart[id]) {
        count = state.cart[id] + 1;
      } else {
        count = 1;
      }
      console.log("here", id, state, count);
      return {
        ...state,
        cart: {
          ...state.cart,
          [id]: count,
        },
      };
    }),

  removeFromCart: (id: IdType) =>
    set((state) => {
      let count = 0;
      remove(id);
      if (state.cart[id]) {
        count = state.cart[id] - 1;
      }
      return {
        ...state,
        cart: {
          ...state.cart,
          [id]: count,
        },
      };
    }),

  fetch: async () => {
    const cart = await load();
    set({
      cart,
    });
  },

  restoreCart: () => {
    const cart = JSON.parse(localStorage.getItem("cart") ?? "[]");
    set({
      cart,
    });
    localStorage.removeItem("cart");
    massAdd(cart);
  },
  clearCart: () => {
    set({
      cart: {},
    });
  },
}));
