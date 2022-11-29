import { useTasks } from "./useTasks";

export default function TaskList() {
  const { items, loading } = useTasks();
  if (loading) return <p>loading…</p>;
  return (
    <ul>
      {items.map((it) => (
        <li key={it.id}>{it.id}</li>
      ))}
    </ul>
  );
}
