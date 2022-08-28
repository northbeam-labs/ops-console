const request = require("supertest");
const app = require("../src/app");

test("user create+list", async () => {
  const c = await request(app).post("/users").send({});
  expect(c.status).toBe(201);
  const l = await request(app).get("/users");
  expect(l.status).toBe(200);
});
