export interface Invoice {
  id: number;
  number: string;
  amount: number;
  currency: string;
  paid: boolean;
}
