const Product = require('../models/productModel');

exports.getProducts = async (req, res) => {
  try {
    const products = await Product.findAll();
    res.status(200).send({ products });
  } catch (err) {
    res.status(500).send({ message: 'Error fetching products', error: err.message });
  }
};

exports.createProduct = async (req, res) => {
  try {
    const product = await Product.create(req.body);
    res.status(201).send({ message: 'Product added successfully', product });
  } catch (err) {
    res.status(500).send({ message: 'Error adding product', error: err.message });
  }
};

exports.deleteProduct = async (req, res) => {
  try {
    const { id } = req.params;
    const deleted = await Product.destroy({ where: { id } });
    if (deleted) {
      res.status(200).send({ message: 'Product deleted successfully' });
    } else {
      res.status(404).send({ message: 'Product not found' });
    }
  } catch (err) {
    res.status(500).send({ message: 'Error deleting product', error: err.message });
  }
};

exports.updateProduct = async (req, res) => {
  try {
    const { id } = req.params;
    const [updated] = await Product.update(req.body, { where: { id } });
    if (updated) {
      res.status(200).send({ message: 'Product updated successfully' });
    } else {
      res.status(404).send({ message: 'Product not found' });
    }
  } catch (err) {
    res.status(500).send({ message: 'Error updating product', error: err.message });
  }
};
