import { api } from "../../lib/api";
import { Webhook } from "./types";

export const listWebhooks = () => api.get<Webhook[]>("/webhooks").then((r) => r.data);
export const getWebhook = (id: number) => api.get<Webhook>(`/webhooks/${id}`).then((r) => r.data);
export const createWebhook = (body: Partial<Webhook>) => api.post<Webhook>("/webhooks", body).then((r) => r.data);
