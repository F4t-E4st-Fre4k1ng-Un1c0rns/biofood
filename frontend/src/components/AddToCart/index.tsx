import Button from "@/components/Button";

interface Props {
  readonly count: number;
  readonly add: () => void;
  readonly remove: () => void;
  readonly className?: string;
}

function AddToCart({ count, add, remove, className }: Props) {
  if (!count) {
    return (
      <Button className={className} color="primary" onClick={add}>
        В корзину!
      </Button>
    );
  }

  return (
    <div className={`flex items-center justify-between ${className ?? ""}`}>
      <Button color="secondary" onClick={remove}>
        -
      </Button>
      <p className="h-fit">{count}</p>
      <Button color="secondary" onClick={add}>
        +
      </Button>
    </div>
  );
}

export default AddToCart;
