import { useEffect, useState } from "react";
import { Payment } from "./types";
import { listPayments } from "./api";

export function usePayments() {
  const [items, setItems] = useState<Payment[]>([]);
  const [loading, setLoading] = useState(true);
  useEffect(() => { listPayments().then(setItems).finally(() => setLoading(false)); }, []);
  return { items, loading };
}
