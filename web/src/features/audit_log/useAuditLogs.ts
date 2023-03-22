import { useEffect, useState } from "react";
import { AuditLog } from "./types";
import { listAuditLogs } from "./api";

export function useAuditLogs() {
  const [items, setItems] = useState<AuditLog[]>([]);
  const [loading, setLoading] = useState(true);
  useEffect(() => { listAuditLogs().then(setItems).finally(() => setLoading(false)); }, []);
  return { items, loading };
}
