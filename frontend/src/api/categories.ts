import Category from "@/types/Category";

export async function load(): Promise<Category[]> {
  if (import.meta.env.VITE_MOCK_API) {
    const answer = await import("./mock/categories.json");
    return answer.default;
  }

  const response = await fetch(
    `${import.meta.env.VITE_API_BASE_URL}/categories`
  );
  const json = await response.json();
  return json.items;
}
