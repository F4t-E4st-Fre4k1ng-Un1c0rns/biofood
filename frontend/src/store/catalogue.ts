import { load as loadCategories } from "@/api/categories";
import { load as loadDishes } from "@/api/dishes";
import Dish from "@/types/Dish";
import LocalCategory from "@/types/LocalCategory";
import { create } from "zustand";

export interface CatalogueStore {
  categories: LocalCategory[];
  dishes: Record<Dish["id"], Dish>;
  loaded: boolean;
  fetch: () => Promise<void>;
}

export const useCatalogueStore = create<CatalogueStore>((set) => ({
  categories: [],
  dishes: {},
  loaded: false,
  fetch: async () => {
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
}));
