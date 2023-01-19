import { api } from "../../lib/api";
import { Invoice } from "./types";

export const listInvoices = () => api.get<Invoice[]>("/invoices").then((r) => r.data);
export const getInvoice = (id: number) => api.get<Invoice>(`/invoices/${id}`).then((r) => r.data);
export const createInvoice = (body: Partial<Invoice>) => api.post<Invoice>("/invoices", body).then((r) => r.data);
