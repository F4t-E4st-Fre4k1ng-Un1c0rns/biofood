import Dish from "@/types/Dish";
import AddToCart from "../AddToCart";

interface Props {
  dish: Dish;
  count: number;
  add?: () => void;
  remove?: () => void;

  showChangeButton?: boolean;
  showPrice?: boolean;
}

export default ({
  dish,
  count,
  add,
  remove,
  showChangeButton,
  showPrice,
}: Props) => {
  return (
    <div className="flex w-full max-w-full justify-between flex-col sm:flex-row gap-4 pb-8">
      <div className="flex gap-4 items-center">
        <img
          src={
            dish.banner ??
            "https://images.unsplash.com/photo-1531234799389-dcb7651eb0a2?q=80&w=200&auto=format"
          }
          alt={dish.name}
          className="size-20 rounded-2xl object-cover"
        />
        <div>
          <h2>{dish.name}</h2>
          <p>{dish.description}</p>
        </div>
      </div>
      <div className="flex gap-4 items-center justify-between sm:justify-end">
        {showPrice ? <p>{dish.price.toLocaleString("ru-RU")}₽</p> : <div></div>}
        {showChangeButton && add && remove ? (
          <AddToCart count={count} add={add} remove={remove} className="w-50" />
        ) : (
          `${count} шт`
        )}
      </div>
    </div>
  );
};
