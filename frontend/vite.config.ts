import { defineConfig } from "vite";
import tailwindcss from "@tailwindcss/vite";
import { URL, fileURLToPath } from "node:url";
import react from "@vitejs/plugin-react";

const ReactCompilerConfig = {};

export default defineConfig({
  plugins: [
    ...tailwindcss(),
    react({
      babel: {
        plugins: [["babel-plugin-react-compiler", ReactCompilerConfig]],
      },
    }),
  ],
  build: {
    rollupOptions: {
      input: {
        main: fileURLToPath(new URL("index.html", import.meta.url)),
        serviceWorker: fileURLToPath(
          new URL("serviceWorker.js", import.meta.url)
        ),
      },
      output: {
        entryFileNames: "[name].js",
      },
    },
  },
  resolve: {
    alias: {
      "@": fileURLToPath(new URL("./src", import.meta.url)),
    },
  },
  server: {
    proxy: {
      "/api": {
        target: "http://localhost:8000/api",
        changeOrigin: true,
        rewrite: (path) => path.replace("/api", ""),
      },
    },
  },
});
