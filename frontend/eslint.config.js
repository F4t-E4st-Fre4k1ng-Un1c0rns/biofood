import globals from "globals";
import pluginJs from "@eslint/js";
import tseslint from "typescript-eslint";
import pluginReact from "eslint-plugin-react";
import eslintPluginPrettierRecommended from "eslint-plugin-prettier/recommended";
import reactHooks from "eslint-plugin-react-hooks";
import reactCompiler from "eslint-plugin-react-compiler";

/** @type {import('eslint').Linter.Config[]} */
export default [
  pluginJs.configs.recommended,
  ...tseslint.configs.strict,
  ...tseslint.configs.stylistic,

  pluginReact.configs.flat.recommended,
  pluginReact.configs.flat["jsx-runtime"],
  reactHooks.configs["recommended-latest"],
  reactCompiler.configs.recommended,

  eslintPluginPrettierRecommended,

  {
    files: ["**/*.{js,mjs,cjs,ts,jsx,tsx}"],
    languageOptions: { globals: globals.browser },
    rules: {
      "id-length": "warn",
      eqeqeq: "warn",
      "dot-notation": "warn",
      "require-unicode-regexp": "error",
      "react-hooks/exhaustive-deps": "off",
      "react/jsx-sort-props": "warn",
      "react/prefer-read-only-props": "warn",
      // TODO: sort-imports and sort-keys
    },
    settings: {
      react: {
        version: "19",
      },
    },
  },
];
