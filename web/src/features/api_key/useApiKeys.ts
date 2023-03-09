import { useEffect, useState } from "react";
import { ApiKey } from "./types";
import { listApiKeys } from "./api";

export function useApiKeys() {
  const [items, setItems] = useState<ApiKey[]>([]);
  const [loading, setLoading] = useState(true);
  useEffect(() => { listApiKeys().then(setItems).finally(() => setLoading(false)); }, []);
  return { items, loading };
}
