import { api } from "../../lib/api";
import { Organization } from "./types";

export const listOrganizations = () => api.get<Organization[]>("/organizations").then((r) => r.data);
export const getOrganization = (id: number) => api.get<Organization>(`/organizations/${id}`).then((r) => r.data);
export const createOrganization = (body: Partial<Organization>) => api.post<Organization>("/organizations", body).then((r) => r.data);
