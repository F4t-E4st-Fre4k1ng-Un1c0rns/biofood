import Categories from "./Category";

export default interface Dish {
  id: string;
  name: string;
  bannerPath: string | undefined;
  price: number;
  description: string | undefined;
  category: Categories["id"];
  weight: number | undefined;
}
