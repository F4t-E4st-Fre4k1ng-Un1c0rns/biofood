import Category from "@/types/Category";
import { useCallback, useState } from "react";
import menuHamburgerIcon from "./icons/menu-hambuger.svg";
import Overlay from "./Overlay";
import Sidebar from "./Sidebar";

interface Props {
  readonly categories: Category[];
  readonly isDrawerOpen: boolean;
  handleDrawerClose(): void;
}

function Drawer({ categories }: Props) {
  const [isDrawerOpen, setDrawerOpen] = useState(false);
  const handleDrawerOpen = useCallback(() => setDrawerOpen(true), []);
  const handleDrawerClose = useCallback(() => setDrawerOpen(false), []);

  return (
    <>
      <img
        className="w-12"
        onClick={handleDrawerOpen}
        src={menuHamburgerIcon}
      />
      <Overlay
        handleDrawerClose={handleDrawerClose}
        isDrawerOpen={isDrawerOpen}
      />
      <Sidebar categories={categories} isDrawerOpen={isDrawerOpen} />
    </>
  );
}

export default Drawer;
