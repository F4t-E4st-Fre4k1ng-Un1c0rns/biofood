import { Route, Routes } from "react-router";
import "./index.css";
import Catalogue from "./pages/Catalogue";
import Cart from "./pages/Cart";
import { useCacheStore } from "./store/cache";
import { Suspense, lazy, useEffect } from "react";
import { useCartStore } from "./store/cart";
import OrderDone from "./pages/OrderDone";
import Main from "./layouts/main";

const Login = lazy(() => import("@/pages/Login"));
const LoginDone = lazy(() => import("@/pages/LoginDone"));
const Account = lazy(() => import("@/pages/Account"));
const NotFound = lazy(() => import("@/pages/NotFound"));

const StaffQrCode = lazy(() => import("@/pages/StaffQrCode"));

export function App() {
  const cache = useCacheStore();
  const cart = useCartStore();

  useEffect(() => {
    cache.fetchCatalogue();
    cart.fetch();
  }, []);

  return (
    <Suspense>
      <Routes>
        <Route element={<Main />} path="/">
          <Route element={<Catalogue />} path="/" />
          <Route element={<Cart />} path="/cart/" />
          <Route element={<OrderDone />} path="/order/:id/" />
          <Route element={<Login />} path="/login/" />
          <Route element={<LoginDone />} path="/login-done/" />
          <Route element={<Account />} path="/account/" />
          <Route element={<StaffQrCode />} path="/account/qr/" />
        </Route>

        <Route element={<NotFound />} path="*" />
      </Routes>
    </Suspense>
  );
}

export default App;
