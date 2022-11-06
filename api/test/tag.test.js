const request = require("supertest");
const app = require("../src/app");

test("tag create+list", async () => {
  const c = await request(app).post("/tags").send({});
  expect(c.status).toBe(201);
  const l = await request(app).get("/tags");
  expect(l.status).toBe(200);
});
