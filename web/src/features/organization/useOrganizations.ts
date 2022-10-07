import { useEffect, useState } from "react";
import { Organization } from "./types";
import { listOrganizations } from "./api";

export function useOrganizations() {
  const [items, setItems] = useState<Organization[]>([]);
  const [loading, setLoading] = useState(true);
  useEffect(() => { listOrganizations().then(setItems).finally(() => setLoading(false)); }, []);
  return { items, loading };
}
