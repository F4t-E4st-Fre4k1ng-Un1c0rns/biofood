import { Route, Routes } from "react-router";
import "../index.css";
import { useCacheStore } from "../store/cache";
import { Suspense, lazy, useEffect } from "react";
import { useCartStore } from "../store/cart";
import NotFound from "@/pages/NotFound";
import sseSubscribeOrders from "@/api/sseOrders";

const ChefKanban = lazy(() => import("@/pos/pages/ChefKanban"));
const PosLogin = lazy(() => import("@/pos/pages/Login"));

export function App() {
  const cache = useCacheStore();
  const cart = useCartStore();

  useEffect(() => {
    cache.fetchCatalogue();
    cart.fetch();
    sseSubscribeOrders(true);
  }, []);

  return (
    <div className="select-none">
      <Suspense>
        <Routes>
          <Route path="/">
            <Route element={<ChefKanban />} path="chef/" />
            <Route element={<PosLogin />} path="login/" />
          </Route>
          <Route element={<NotFound />} path="*" />
        </Routes>
      </Suspense>
    </div>
  );
}

export default App;
