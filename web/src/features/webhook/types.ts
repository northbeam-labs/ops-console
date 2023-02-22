export interface Webhook {
  id: number;
  url: string;
  event: string;
  active: boolean;
  secret: string;
}
