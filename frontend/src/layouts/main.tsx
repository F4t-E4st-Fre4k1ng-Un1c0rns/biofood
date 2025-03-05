import Header from "@/components/Header";
import { useCacheStore } from "@/store/cache";
import { Outlet } from "react-router";

export default () => {
  const catalogue = useCacheStore();
  return (
    <>
      <Header categories={catalogue.categories} />
      <div className="p-8">
        <Outlet />
      </div>
    </>
  );
};
