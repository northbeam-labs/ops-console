import axios from "axios";

export const api = axios.create({ baseURL: import.meta.env.VITE_API ?? "http://localhost:8000" });

api.interceptors.response.use(
  (r) => r,
  (e) => Promise.reject(e?.response?.data ?? e)
);
