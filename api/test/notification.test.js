const request = require("supertest");
const app = require("../src/app");

test("notification create+list", async () => {
  const c = await request(app).post("/notifications").send({});
  expect(c.status).toBe(201);
  const l = await request(app).get("/notifications");
  expect(l.status).toBe(200);
});
