const request = require("supertest");
const app = require("../src/app");

test("api_key create+list", async () => {
  const c = await request(app).post("/api_keys").send({});
  expect(c.status).toBe(201);
  const l = await request(app).get("/api_keys");
  expect(l.status).toBe(200);
});
