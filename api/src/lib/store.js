class Store {
  constructor() { this.rows = []; this.seq = 1; }
  list() { return this.rows; }
  get(id) { return this.rows.find((r) => r.id === Number(id)); }
  create(data) { const row = { id: this.seq++, ...data }; this.rows.push(row); return row; }
  remove(id) { this.rows = this.rows.filter((r) => r.id !== Number(id)); }
}
module.exports = Store;
