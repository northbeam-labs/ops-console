import { api } from "../../lib/api";
import { User } from "./types";

export const listUsers = () => api.get<User[]>("/users").then((r) => r.data);
export const getUser = (id: number) => api.get<User>(`/users/${id}`).then((r) => r.data);
export const createUser = (body: Partial<User>) => api.post<User>("/users", body).then((r) => r.data);
