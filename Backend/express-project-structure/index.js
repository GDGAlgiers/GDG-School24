const express = require("express");
const ProductRouter = require("./routes/ProductRoutes")

const app = express();

app.use((req,res,next) => {
  console.log("Middleware 1");
  next();
})

app.use(express.json());

app.use(ProductRouter);

app.listen(3000, function () {
  console.log("Example app listening on port 3000!");
});
