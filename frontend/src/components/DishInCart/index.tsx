import Dish from "@/types/Dish";
import AddToCart from "../AddToCart";

interface Props {
  readonly dish: Dish;
  readonly count: number;
  readonly add?: () => void;
  readonly remove?: () => void;

  readonly showChangeButton?: boolean;
  readonly showPrice?: boolean;
  readonly showImage?: boolean;
}

function DishInCart({
  dish,
  count,
  add,
  remove,
  showChangeButton,
  showPrice,
  showImage,
}: Props) {
  return (
    <div className="flex w-full max-w-full justify-between flex-col sm:flex-row gap-4 pb-4">
      <div className="flex gap-4 items-center">
        {showImage && (
          <img
            alt={dish.name}
            className="size-20 rounded-2xl object-cover"
            src={
              dish.bannerPath ??
              "https://images.unsplash.com/photo-1531234799389-dcb7651eb0a2?q=80&w=200&auto=format"
            }
          />
        )}
        <div>
          <h2>{dish.name}</h2>
          <p>{dish.description}</p>
        </div>
      </div>
      <div className="flex gap-4 items-center justify-between sm:justify-end">
        {showPrice ? <p>{dish.price.toLocaleString("ru-RU")}₽</p> : <div />}
        {showChangeButton && add && remove ? (
          <AddToCart add={add} className="w-50" count={count} remove={remove} />
        ) : (
          `${count} шт`
        )}
      </div>
    </div>
  );
}
export default DishInCart;
