const request = require("supertest");
const app = require("../src/app");

test("organization create+list", async () => {
  const c = await request(app).post("/organizations").send({});
  expect(c.status).toBe(201);
  const l = await request(app).get("/organizations");
  expect(l.status).toBe(200);
});
