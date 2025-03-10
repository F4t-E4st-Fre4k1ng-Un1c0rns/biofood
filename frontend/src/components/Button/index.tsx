import { MouseEventHandler } from "react";

interface Props {
  readonly children: string;
  readonly color: "primary" | "secondary" | "accent";
  readonly onClick?: MouseEventHandler<HTMLButtonElement>;
  readonly className?: string;
}

const colors = {
  primary: "bg-primary text-white",
  secondary: "bg-secondary text-black",
  accent: "bg-accent text-white",
};
function Button({ children, onClick, color, className }: Props) {
  return (
    <button
      className={`rounded-xl bg-accent h-fit ${className ?? ""}`}
      onClick={onClick}
    >
      <div
        className={`p-4 rounded-xl ${colors[color]} hover:translate-(--button-offset)`}
      >
        {children}
      </div>
    </button>
  );
}

export default Button;
