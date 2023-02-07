import { usePayments } from "./usePayments";

export default function PaymentList() {
  const { items, loading } = usePayments();
  if (loading) return <p>loading…</p>;
  return (
    <ul>
      {items.map((it) => (
        <li key={it.id}>{it.id}</li>
      ))}
    </ul>
  );
}
