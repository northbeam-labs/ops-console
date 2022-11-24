const request = require("supertest");
const app = require("../src/app");

test("invoice create+list", async () => {
  const c = await request(app).post("/invoices").send({});
  expect(c.status).toBe(201);
  const l = await request(app).get("/invoices");
  expect(l.status).toBe(200);
});
