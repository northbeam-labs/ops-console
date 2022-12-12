const request = require("supertest");
const app = require("../src/app");

test("webhook create+list", async () => {
  const c = await request(app).post("/webhooks").send({});
  expect(c.status).toBe(201);
  const l = await request(app).get("/webhooks");
  expect(l.status).toBe(200);
});
