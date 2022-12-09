import { useEffect, useState } from "react";
import { Comment } from "./types";
import { listComments } from "./api";

export function useComments() {
  const [items, setItems] = useState<Comment[]>([]);
  const [loading, setLoading] = useState(true);
  useEffect(() => { listComments().then(setItems).finally(() => setLoading(false)); }, []);
  return { items, loading };
}
