import { useEffect, useState } from "react";
import { Notification } from "./types";
import { listNotifications } from "./api";

export function useNotifications() {
  const [items, setItems] = useState<Notification[]>([]);
  const [loading, setLoading] = useState(true);
  useEffect(() => { listNotifications().then(setItems).finally(() => setLoading(false)); }, []);
  return { items, loading };
}
