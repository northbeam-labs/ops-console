const express = require("express");
const cors = require("cors");
const helmet = require("helmet");
const morgan = require("morgan");
const errors = require("./middleware/errors");

const app = express();
app.use(helmet());
app.use(cors());
app.use(morgan("tiny"));
app.use(express.json());

app.get("/health", (_req, res) => res.json({ status: "ok" }));

app.use("/users", require("./routes/user"));
app.use("/organizations", require("./routes/organization"));
app.use("/projects", require("./routes/project"));
app.use("/tasks", require("./routes/task"));
app.use("/comments", require("./routes/comment"));
app.use("/tags", require("./routes/tag"));
app.use("/invoices", require("./routes/invoice"));
app.use("/payments", require("./routes/payment"));
app.use("/notifications", require("./routes/notification"));
app.use("/webhooks", require("./routes/webhook"));
app.use("/api_keys", require("./routes/api_key"));
app.use("/audit_logs", require("./routes/audit_log"));

app.use(errors);
module.exports = app;
