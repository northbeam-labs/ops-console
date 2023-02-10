import { api } from "../../lib/api";
import { Notification } from "./types";

export const listNotifications = () => api.get<Notification[]>("/notifications").then((r) => r.data);
export const getNotification = (id: number) => api.get<Notification>(`/notifications/${id}`).then((r) => r.data);
export const createNotification = (body: Partial<Notification>) => api.post<Notification>("/notifications", body).then((r) => r.data);
