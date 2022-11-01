import { useEffect, useState } from "react";
import { Project } from "./types";
import { listProjects } from "./api";

export function useProjects() {
  const [items, setItems] = useState<Project[]>([]);
  const [loading, setLoading] = useState(true);
  useEffect(() => { listProjects().then(setItems).finally(() => setLoading(false)); }, []);
  return { items, loading };
}
