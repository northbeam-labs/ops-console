export interface AuditLog {
  id: number;
  action: string;
  actor_id: number;
  target: string;
}
