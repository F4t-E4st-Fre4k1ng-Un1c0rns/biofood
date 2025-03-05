import OrderStatus from "@/types/OrderStatus";

export const names = {
  [OrderStatus.accepted]: "Подтвержден",
  [OrderStatus.canceled]: "Отменен",
  [OrderStatus.cooking]: "Готовится",
  [OrderStatus.pending]: "Ожидает подтверждения",
  [OrderStatus.ready]: "Готов",
  [OrderStatus.taken]: "Выдан",
};

export const colorClasses = {
  [OrderStatus.accepted]: "bg-secondary text-black",
  [OrderStatus.canceled]: "bg-white text-black",
  [OrderStatus.cooking]: "bg-accent text-white",
  [OrderStatus.pending]: "bg-secondary text-black",
  [OrderStatus.ready]: "bg-primary text-white",
  [OrderStatus.taken]: "bg-white text-black",
};
