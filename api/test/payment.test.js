const request = require("supertest");
const app = require("../src/app");

test("payment create+list", async () => {
  const c = await request(app).post("/payments").send({});
  expect(c.status).toBe(201);
  const l = await request(app).get("/payments");
  expect(l.status).toBe(200);
});
