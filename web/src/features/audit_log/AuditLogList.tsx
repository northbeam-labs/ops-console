import { useAuditLogs } from "./useAuditLogs";

export default function AuditLogList() {
  const { items, loading } = useAuditLogs();
  if (loading) return <p>loading…</p>;
  return (
    <ul>
      {items.map((it) => (
        <li key={it.id}>{it.id}</li>
      ))}
    </ul>
  );
}
