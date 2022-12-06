import { api } from "../../lib/api";
import { Comment } from "./types";

export const listComments = () => api.get<Comment[]>("/comments").then((r) => r.data);
export const getComment = (id: number) => api.get<Comment>(`/comments/${id}`).then((r) => r.data);
export const createComment = (body: Partial<Comment>) => api.post<Comment>("/comments", body).then((r) => r.data);
