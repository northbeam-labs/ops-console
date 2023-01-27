import { useInvoices } from "./useInvoices";

export default function InvoiceList() {
  const { items, loading } = useInvoices();
  if (loading) return <p>loading…</p>;
  return (
    <ul>
      {items.map((it) => (
        <li key={it.id}>{it.id}</li>
      ))}
    </ul>
  );
}
