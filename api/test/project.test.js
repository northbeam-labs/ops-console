const request = require("supertest");
const app = require("../src/app");

test("project create+list", async () => {
  const c = await request(app).post("/projects").send({});
  expect(c.status).toBe(201);
  const l = await request(app).get("/projects");
  expect(l.status).toBe(200);
});
