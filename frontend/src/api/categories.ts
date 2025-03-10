import Category from "@/types/Category";

export async function load(): Promise<Category[]> {
  const response = await fetch(
    `${import.meta.env.VITE_API_BASE_URL}/categories`
  );
  const json = await response.json();
  return json.items;
}
