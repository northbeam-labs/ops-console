const router = require("express").Router();
const c = require("../controllers/payment");
const wrap = require("../lib/asyncHandler");

router.get("/", wrap(c.list));
router.get("/:id", wrap(c.get));
router.post("/", wrap(c.create));
router.delete("/:id", wrap(c.remove));

module.exports = router;
