const Store = require("../lib/store");
const store = new Store();
const FIELDS = ["label", "color"];

exports.list = (_req, res) => res.json(store.list());
exports.get = (req, res) => { const row = store.get(req.params.id); return row ? res.json(row) : res.status(404).json({ error: "not found" }); };
exports.create = (req, res) => { const data = {}; FIELDS.forEach((k) => (data[k] = req.body[k])); res.status(201).json(store.create(data)); };
exports.remove = (req, res) => { store.remove(req.params.id); res.status(204).end(); };
