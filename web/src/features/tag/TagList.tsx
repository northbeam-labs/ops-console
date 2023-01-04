import { useTags } from "./useTags";

export default function TagList() {
  const { items, loading } = useTags();
  if (loading) return <p>loading…</p>;
  return (
    <ul>
      {items.map((it) => (
        <li key={it.id}>{it.id}</li>
      ))}
    </ul>
  );
}
