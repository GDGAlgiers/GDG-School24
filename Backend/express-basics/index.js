const express = require("express");
const app = express();


const products =[
  {
    id: 1,
    name: "Apple",
    price: 0.5,
  },
]

app.use((req,res,next) => {
  console.log("Middleware 1");
  next();
})




app.use(express.json());


app.post("/products", function (req, res) {
  const product = req.body;
  products.push(product);
  res.status(201).send({ message: "Product added successfully" });
} );

app.get("/products", function (req, res) {
  res.status(200).send({ products: products });
});

app.delete("/products/:id", function (req, res) {
  const id = req.params.id;
  const index = products.findIndex((product) => product.id == id);
  if (index != -1) {
    products.splice(index, 1);
    res.status(200).send({ message: "Product deleted successfully!!!" });
  } else {
    res.status(404).send({ message: "Product not found" });
  }
});

app.put("/products/:id", function (req, res) {
  const id = req.params.id;
  const product = req.body;
  const index = products.findIndex((product) => product.id == id);
  if (index != -1) {
    products[index] = product;
    res.status(200).send({ message: "Product updated successfully" });
  } else {
    res.status(404).send({ message: "Product not found" });
  }
} );



app.listen(3000, function () {
  console.log("Example app listening on port 3000!");
});