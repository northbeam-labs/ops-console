import { api } from "../../lib/api";
import { Tag } from "./types";

export const listTags = () => api.get<Tag[]>("/tags").then((r) => r.data);
export const getTag = (id: number) => api.get<Tag>(`/tags/${id}`).then((r) => r.data);
export const createTag = (body: Partial<Tag>) => api.post<Tag>("/tags", body).then((r) => r.data);
