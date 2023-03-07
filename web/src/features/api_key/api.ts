import { api } from "../../lib/api";
import { ApiKey } from "./types";

export const listApiKeys = () => api.get<ApiKey[]>("/api_keys").then((r) => r.data);
export const getApiKey = (id: number) => api.get<ApiKey>(`/api_keys/${id}`).then((r) => r.data);
export const createApiKey = (body: Partial<ApiKey>) => api.post<ApiKey>("/api_keys", body).then((r) => r.data);
