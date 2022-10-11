import { useOrganizations } from "./useOrganizations";

export default function OrganizationList() {
  const { items, loading } = useOrganizations();
  if (loading) return <p>loading…</p>;
  return (
    <ul>
      {items.map((it) => (
        <li key={it.id}>{it.id}</li>
      ))}
    </ul>
  );
}
