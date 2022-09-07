import { useUsers } from "./useUsers";

export default function UserList() {
  const { items, loading } = useUsers();
  if (loading) return <p>loading…</p>;
  return (
    <ul>
      {items.map((it) => (
        <li key={it.id}>{it.id}</li>
      ))}
    </ul>
  );
}
