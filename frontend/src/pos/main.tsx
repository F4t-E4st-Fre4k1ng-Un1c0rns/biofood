import { createRoot } from "react-dom/client";
import { App } from "./App";
import { HashRouter } from "react-router";

function start() {
  const rootElement = document.getElementById("root");
  if (!rootElement) {
    console.error("Root element not found");
    return;
  }

  const root = createRoot(rootElement);
  root.render(
    <HashRouter>
      <App />
    </HashRouter>
  );
}

if (document.readyState === "loading") {
  document.addEventListener("DOMContentLoaded", start);
} else {
  start();
}
