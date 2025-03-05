import Order from "@/types/Order";
import { colorClasses, names } from "./consts";

interface Props {
  status: Order["status"];
}

export default ({ status }: Props) => {
  return (
    <p className={`${colorClasses[status]} w-fit py-1 px-2 rounded-2xl`}>
      {names[status]}
    </p>
  );
};
