import { useEffect, useState } from "react";
import { Invoice } from "./types";
import { listInvoices } from "./api";

export function useInvoices() {
  const [items, setItems] = useState<Invoice[]>([]);
  const [loading, setLoading] = useState(true);
  useEffect(() => { listInvoices().then(setItems).finally(() => setLoading(false)); }, []);
  return { items, loading };
}
