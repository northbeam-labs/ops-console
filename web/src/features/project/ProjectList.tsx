import { useProjects } from "./useProjects";

export default function ProjectList() {
  const { items, loading } = useProjects();
  if (loading) return <p>loading…</p>;
  return (
    <ul>
      {items.map((it) => (
        <li key={it.id}>{it.id}</li>
      ))}
    </ul>
  );
}
