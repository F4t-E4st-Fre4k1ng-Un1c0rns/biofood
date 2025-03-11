import sseSubscribeOrders from "@/api/sseOrders";
import Header from "@/components/Header";
import { useCacheStore } from "@/store/cache";
import { useEffect } from "react";
import { Outlet } from "react-router";

function Layout() {
  const catalogue = useCacheStore();

  useEffect(() => {
    sseSubscribeOrders();
  }, []);

  return (
    <>
      <Header categories={catalogue.categories} />
      <div className="p-8">
        <Outlet />
      </div>
    </>
  );
}

export default Layout;
