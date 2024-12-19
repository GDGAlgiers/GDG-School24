const ProductModel = require("../models/productModel");

const createProducts = function (req, res) {
  const product = req.body;
  ProductModel.addToProducts(product);
  res.status(201).send({ message: "Product added successfully" });
};

const getProducts = function (req, res) {
  const products = ProductModel.getProducts();
  res.status(200).send({ products: products });
};

const deleteProduct = function (req, res) {
  const id = req.params.id;
  const success = ProductModel.deleteProductById(id);
  if (success) {
    res.status(200).send({ message: "Product deleted successfully!!!" });
  } else {
    res.status(404).send({ message: "Product not found" });
  }
};

const updateProduct = function (req, res) {
  const id = req.params.id;
  const product = req.body;
  const success = ProductModel.updateProductById(id, product);
  if (success) {
    res.status(200).send({ message: "Product updated successfully" });
  } else {
    res.status(404).send({ message: "Product not found" });
  }
};

module.exports = {
  createProducts,
  getProducts,
  deleteProduct,
  updateProduct,
};