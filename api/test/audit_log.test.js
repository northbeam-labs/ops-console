const request = require("supertest");
const app = require("../src/app");

test("audit_log create+list", async () => {
  const c = await request(app).post("/audit_logs").send({});
  expect(c.status).toBe(201);
  const l = await request(app).get("/audit_logs");
  expect(l.status).toBe(200);
});
