import { useComments } from "./useComments";

export default function CommentList() {
  const { items, loading } = useComments();
  if (loading) return <p>loading…</p>;
  return (
    <ul>
      {items.map((it) => (
        <li key={it.id}>{it.id}</li>
      ))}
    </ul>
  );
}
