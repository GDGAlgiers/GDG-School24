const express = require("express");
const app = express();
const productRoutes = require("./routes/productRoutes");

const PORT = 3000;

app.use(express.json()); 

// Routes
app.use("/products", productRoutes);


app.listen(PORT, () => {
  console.log(`Server running on port ${PORT}`);
});
