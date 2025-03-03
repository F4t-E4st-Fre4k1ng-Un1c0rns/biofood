import { load } from "@/api/authenticate";
import User, { Roles } from "@/types/User";
import { create } from "zustand";

export interface AuthStore {
  loggedIn: boolean;
  user: User | null;
  auth: (token: string) => Promise<User>;
  logout: () => void;
}

export const useAuthStore = create<AuthStore>((set) => ({
  loggedIn: localStorage.getItem("user") !== null,
  user: JSON.parse(localStorage.getItem("user") ?? "null"),
  auth: async (token: string) => {
    const user = await load(token);
    set({
      loggedIn: true,
      user,
    });
    localStorage.setItem("user", JSON.stringify(user));
    return user;
  },
  logout: () => {
    set({
      loggedIn: false,
      user: null,
    });
    localStorage.removeItem("user");
  },
}));
