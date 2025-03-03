import Dish from "./Dish";
import OrderStatus from "./OrderStatus";

export default interface Order {
  id: string;
  items: {
    dish: Dish;
    amount: number;
  }[];
  status: OrderStatus;
  takeoutTime: Date;
}
