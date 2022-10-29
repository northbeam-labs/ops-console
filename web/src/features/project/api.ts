import { api } from "../../lib/api";
import { Project } from "./types";

export const listProjects = () => api.get<Project[]>("/projects").then((r) => r.data);
export const getProject = (id: number) => api.get<Project>(`/projects/${id}`).then((r) => r.data);
export const createProject = (body: Partial<Project>) => api.post<Project>("/projects", body).then((r) => r.data);
