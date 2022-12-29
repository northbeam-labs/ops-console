import { useEffect, useState } from "react";
import { Tag } from "./types";
import { listTags } from "./api";

export function useTags() {
  const [items, setItems] = useState<Tag[]>([]);
  const [loading, setLoading] = useState(true);
  useEffect(() => { listTags().then(setItems).finally(() => setLoading(false)); }, []);
  return { items, loading };
}
