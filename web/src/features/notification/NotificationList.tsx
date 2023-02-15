import { useNotifications } from "./useNotifications";

export default function NotificationList() {
  const { items, loading } = useNotifications();
  if (loading) return <p>loading…</p>;
  return (
    <ul>
      {items.map((it) => (
        <li key={it.id}>{it.id}</li>
      ))}
    </ul>
  );
}
