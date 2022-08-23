import { create } from "zustand";

interface AuthState { token: string | null; setToken: (t: string | null) => void; }

export const useAuth = create<AuthState>((set) => ({
  token: localStorage.getItem("token"),
  setToken: (token) => { token ? localStorage.setItem("token", token) : localStorage.removeItem("token"); set({ token }); },
}));
