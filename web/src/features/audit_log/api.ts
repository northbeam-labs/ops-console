import { api } from "../../lib/api";
import { AuditLog } from "./types";

export const listAuditLogs = () => api.get<AuditLog[]>("/audit_logs").then((r) => r.data);
export const getAuditLog = (id: number) => api.get<AuditLog>(`/audit_logs/${id}`).then((r) => r.data);
export const createAuditLog = (body: Partial<AuditLog>) => api.post<AuditLog>("/audit_logs", body).then((r) => r.data);
