import { createRoot } from "react-dom/client";
import { App } from "./App";
import { BrowserRouter } from "react-router";

function start() {
  const root = createRoot(document.getElementById("root")!);
  root.render(
    <BrowserRouter>
      <App />
    </BrowserRouter>
  );
}

if (document.readyState === "loading") {
  document.addEventListener("DOMContentLoaded", start);
} else {
  start();
}
