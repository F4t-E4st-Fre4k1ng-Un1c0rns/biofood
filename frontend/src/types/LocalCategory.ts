import Category from "./Category";
import Dish from "./Dish";

type LocalCategory = Category & {
  loaded: boolean;
  dishes: Dish["id"][];
};
export default LocalCategory;
