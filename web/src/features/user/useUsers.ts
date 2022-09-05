import { useEffect, useState } from "react";
import { User } from "./types";
import { listUsers } from "./api";

export function useUsers() {
  const [items, setItems] = useState<User[]>([]);
  const [loading, setLoading] = useState(true);
  useEffect(() => { listUsers().then(setItems).finally(() => setLoading(false)); }, []);
  return { items, loading };
}
