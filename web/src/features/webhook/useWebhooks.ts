import { useEffect, useState } from "react";
import { Webhook } from "./types";
import { listWebhooks } from "./api";

export function useWebhooks() {
  const [items, setItems] = useState<Webhook[]>([]);
  const [loading, setLoading] = useState(true);
  useEffect(() => { listWebhooks().then(setItems).finally(() => setLoading(false)); }, []);
  return { items, loading };
}
