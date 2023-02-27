import { useWebhooks } from "./useWebhooks";

export default function WebhookList() {
  const { items, loading } = useWebhooks();
  if (loading) return <p>loading…</p>;
  return (
    <ul>
      {items.map((it) => (
        <li key={it.id}>{it.id}</li>
      ))}
    </ul>
  );
}
