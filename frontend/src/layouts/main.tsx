import sseSubscribeOrders from "@/api/sseOrders";
import Header from "@/components/Header";
import LoadingIcon from "@/components/LoadingIcon";
import { useCacheStore } from "@/store/cache";
import { Suspense, useEffect } from "react";
import { Outlet, useLocation } from "react-router";

function Layout() {
  const catalogue = useCacheStore();
  const location = useLocation();

  useEffect(() => {
    sseSubscribeOrders();
  }, []);

  return (
    <>
      <Header categories={catalogue.categories} />
      <div className="p-8">
        <Suspense fallback={<LoadingIcon />} key={location.key}>
          <Outlet />
        </Suspense>
      </div>
    </>
  );
}

export default Layout;
