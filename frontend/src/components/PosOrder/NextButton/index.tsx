import Button from "@/components/Button";
import OrderStatus from "@/types/OrderStatus";

interface Props {
  status: OrderStatus;
  setStatus: (status: OrderStatus) => void;
}

const ACCEPT_BUTTON_TEXT = {
  [OrderStatus.pending]: "Принять",
  [OrderStatus.accepted]: "Готовится",
  [OrderStatus.cooking]: "Готово",
  [OrderStatus.ready]: "Выдано",
  [OrderStatus.canceled]: "",
  [OrderStatus.taken]: "",
};

const NEXT_STATUS = {
  [OrderStatus.pending]: OrderStatus.accepted,
  [OrderStatus.accepted]: OrderStatus.cooking,
  [OrderStatus.cooking]: OrderStatus.ready,
  [OrderStatus.ready]: OrderStatus.taken,
  [OrderStatus.canceled]: OrderStatus.canceled,
  [OrderStatus.taken]: OrderStatus.taken,
};

export default ({ status, setStatus }: Props) => {
  return (
    <div>
      {status == OrderStatus.pending && (
        <Button
          color="secondary"
          className="mr-1"
          onClick={() => setStatus(OrderStatus.canceled)}
        >
          Отменить
        </Button>
      )}
      <Button color="primary" onClick={() => setStatus(NEXT_STATUS[status])}>
        {ACCEPT_BUTTON_TEXT[status]}
      </Button>
    </div>
  );
};
