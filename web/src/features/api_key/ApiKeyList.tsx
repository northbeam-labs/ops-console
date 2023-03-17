import { useApiKeys } from "./useApiKeys";

export default function ApiKeyList() {
  const { items, loading } = useApiKeys();
  if (loading) return <p>loading…</p>;
  return (
    <ul>
      {items.map((it) => (
        <li key={it.id}>{it.id}</li>
      ))}
    </ul>
  );
}
