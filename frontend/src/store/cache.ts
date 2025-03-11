import { load as loadCategories } from "@/api/categories";
import { load as loadDishes } from "@/api/dishes";
import Dish from "@/types/Dish";
import LocalCategory from "@/types/LocalCategory";
import Order from "@/types/Order";
import { create } from "zustand";

export interface CacheStore {
  categories: LocalCategory[];
  dishes: Record<Dish["id"], Dish>;
  orders: Record<Order["id"], Order>;
  loaded: boolean;
  fetchCatalogue: () => Promise<void>;
  setCachedOrders: (orders: Order[]) => void;
}

export const useCacheStore = create<CacheStore>((set) => ({
  categories: [],
  dishes: {},
  orders: {},
  loaded: false,
  fetchCatalogue: async () => {
    set({
      loaded: false,
    });
    const categories = await loadCategories();
    Promise.all(
      categories.map(async (category, index) => {
        set((state) => ({
          ...state,
          categories: [
            ...state.categories,
            {
              ...category,
              loaded: false,
              dishes: [],
            },
          ],
        }));

        const dishes = await loadDishes(category.id);
        const dishRecords = Object.fromEntries(
          dishes.map((dish) => [dish.id, dish])
        );
        set((state) => {
          const fixedCategories = state.categories;
          fixedCategories[index].loaded = true;
          fixedCategories[index].dishes = Object.keys(dishRecords);
          return {
            ...state,
            categories: fixedCategories,
            dishes: {
              ...state.dishes,
              ...dishRecords,
            },
          };
        });
      })
    );
  },
  setCachedOrders: (orders: Order[]) => {
    set((state) => ({
      ...state,
      orders: {
        ...state.orders,
        ...Object.fromEntries(orders.map((order) => [order.id, order])),
      },
    }));
  },
}));

export const cacheStore = () => useCacheStore;
