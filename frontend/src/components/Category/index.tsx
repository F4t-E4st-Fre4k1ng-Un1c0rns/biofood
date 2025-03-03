import LocalCategory from "@/types/LocalCategory";
import LoadingIcon from "../LoadingIcon";
import { useCatalogueStore } from "@/store/catalogue";
import DishPreview from "../DishPreview";
import { useCartStore } from "@/store/cart";

interface Props {
  category: LocalCategory;
  id: string;
}

export default ({ category, id }: Props) => {
  const catalogue = useCatalogueStore();
  const cart = useCartStore();
  return (
    <>
      <h1 id={id} className="not-first:pt-8">
        {category.name}
      </h1>
      {!category.loaded && <LoadingIcon />}
      <div className="grid grid-cols-[repeat(auto-fill,minmax(20rem,auto))] gap-4 justify-around">
        {category.loaded &&
          category.dishes.map((dishId) => {
            const add = () => {
              cart.addToCart(dishId);
            };
            const remove = () => {
              cart.removeFromCart(dishId);
            };
            return (
              <DishPreview
                dish={catalogue.dishes[dishId]}
                count={cart.cart[dishId]}
                add={add}
                remove={remove}
                key={dishId}
              />
            );
          })}
      </div>
    </>
  );
};
