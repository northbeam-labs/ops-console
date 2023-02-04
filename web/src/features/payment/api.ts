import { api } from "../../lib/api";
import { Payment } from "./types";

export const listPayments = () => api.get<Payment[]>("/payments").then((r) => r.data);
export const getPayment = (id: number) => api.get<Payment>(`/payments/${id}`).then((r) => r.data);
export const createPayment = (body: Partial<Payment>) => api.post<Payment>("/payments", body).then((r) => r.data);
