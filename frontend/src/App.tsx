import { Route, Routes } from "react-router";
import Header from "./components/Header";
import "./index.css";
import Catalogue from "./pages/Catalogue";
import Cart from "./pages/Cart";
import { useCatalogueStore } from "./store/catalogue";
import { lazy, Suspense, useEffect } from "react";
import { useCartStore } from "./store/cart";
import OrderDone from "./pages/OrderDone";
import NotFound from "./pages/NotFound";

const Login = lazy(() => import("@/pages/Login"));
const LoginDone = lazy(() => import("@/pages/LoginDone"));
const Account = lazy(() => import("@/pages/Account"));

export function App() {
  const catalogue = useCatalogueStore();
  const cart = useCartStore();

  useEffect(() => {
    catalogue.fetch();
    cart.fetch();
  }, []);

  return (
    <>
      <Header categories={catalogue.categories} />
      <div className="p-8">
        <Suspense>
          <Routes>
            <Route path="/" element={<Catalogue />} />
            <Route path="/cart/" element={<Cart />} />
            <Route path="/order-done/" element={<OrderDone />} />
            <Route path="/login/" element={<Login />} />
            <Route path="/login-done/" element={<LoginDone />} />
            <Route path="/account/" element={<Account />} />
            <Route path="*" element={<NotFound />} />
          </Routes>
        </Suspense>
      </div>
    </>
  );
}

export default App;
