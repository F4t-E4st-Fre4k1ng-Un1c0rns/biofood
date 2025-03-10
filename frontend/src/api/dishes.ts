import Category from "@/types/Category";
import Dish from "@/types/Dish";

export async function load(category_id: Category["id"]): Promise<Dish[]> {
  const params = new URLSearchParams({
    category_id,
  });
  const response = await fetch(
    `${import.meta.env.VITE_API_BASE_URL}/dishes?${params}`
  );
  const json = await response.json();
  return json.items;
}
