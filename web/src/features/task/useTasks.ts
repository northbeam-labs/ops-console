import { useEffect, useState } from "react";
import { Task } from "./types";
import { listTasks } from "./api";

export function useTasks() {
  const [items, setItems] = useState<Task[]>([]);
  const [loading, setLoading] = useState(true);
  useEffect(() => { listTasks().then(setItems).finally(() => setLoading(false)); }, []);
  return { items, loading };
}
