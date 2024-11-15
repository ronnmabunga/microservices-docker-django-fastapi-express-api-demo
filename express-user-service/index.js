const express = require("express");
const app = express();
const PORT = 8003;

app.get("/auth", (req, res) => {
    res.status(200).send({ message: "User Authentication Service" });
});

app.listen(PORT, () => {
    console.log(`Express Auth & Profile Service listening at http://localhost:${PORT}`);
});
