import Category from "@/types/Category";
import { Link } from "react-router";
import { HashLink } from "react-router-hash-link";
import shoppingCartIcon from "./icons/shopping-cart.svg";
import userIcon from "./icons/user.svg";
import unknownUserIcon from "./icons/unknown-user.svg";
import { useAuthStore } from "@/store/auth";
import { useMediaQuery } from "usehooks-ts";
import Drawer from "./Drawer";

interface Props {
  readonly categories: Category[];
}

function Header({ categories }: Props) {
  const auth = useAuthStore();
  const isDesktop = useMediaQuery("(min-width: 48rem)");

  if (isDesktop) {
    return (
      <header className="w-full flex justify-between gap-6 p-8 sticky top-0 bg-white items-end">
        <HashLink className="text-xl font-medium" to="/#">
          Биофуд
        </HashLink>
        <nav className="w-full flex gap-6 text-nowrap overflow-scroll mx-5">
          {categories.map((category) => (
            <HashLink key={category.id} to={`/#${category.id}`}>
              {category.name}
            </HashLink>
          ))}
        </nav>
        <Link to="/cart/">
          <img src={shoppingCartIcon} />
        </Link>
        {auth.loggedIn ? (
          <Link to="/account">
            <img className="hover:text-primary" src={userIcon} />
          </Link>
        ) : (
          <Link to="/login">
            <img className="hover:text-primary" src={unknownUserIcon} />
          </Link>
        )}
      </header>
    );
  }
  return (
    <header className="w-full flex justify-between gap-6 p-8 sticky top-0 bg-white items-center">
      <Drawer categories={categories}/>
      <HashLink className="ml-6 text-xl font-semibold" to="/#">
        Биофуд
      </HashLink>
      <div className="flex gap-4">
        <Link to="/cart/">
          <img className="w-6 hover:text-primary" src={shoppingCartIcon} />
        </Link>
        {auth.loggedIn ? (
          <Link to="/account">
            <img className="w-6 hover:text-primary" src={userIcon} />
          </Link>
        ) : (
          <Link to="/login">
            <img className="w-6 hover:text-primary" src={unknownUserIcon} />
          </Link>
        )}
      </div>
    </header>
  );
}
export default Header;
