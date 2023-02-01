export interface Payment {
  id: number;
  amount: number;
  provider: string;
  status: string;
  reference: string;
}
