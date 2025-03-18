import Category from "@/types/Category";
import { HashLink } from "react-router-hash-link";

interface Props {
  readonly categories: Category[];
  readonly isDrawerOpen: boolean;
}

function Sidebar({ categories, isDrawerOpen }: Props) {
  return (
    <>
      <div
        className={`fixed left-0 top-0 h-screen z-10 bg-white p-8
        ease-in-out duration-300
        ${isDrawerOpen ? "translate-0" : "-translate-x-1/1"}`}
      >
        <h1>Блюда</h1>
        <nav className="flex flex-col gap-5 my-5">
          {categories.map((category) => (
            <HashLink key={category.id} to={`/#${category.id}`}>
              {category.name}
            </HashLink>
          ))}
        </nav>
      </div>
    </>
  );
}

export default Sidebar;
