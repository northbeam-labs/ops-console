import { api } from "../../lib/api";
import { Task } from "./types";

export const listTasks = () => api.get<Task[]>("/tasks").then((r) => r.data);
export const getTask = (id: number) => api.get<Task>(`/tasks/${id}`).then((r) => r.data);
export const createTask = (body: Partial<Task>) => api.post<Task>("/tasks", body).then((r) => r.data);
