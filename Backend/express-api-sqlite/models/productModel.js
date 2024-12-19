const { DataTypes } = require('sequelize');
const sequelize = require('../config/databse');

// Define Product model
const Product = sequelize.define('Product', {
  name: {
    type: DataTypes.STRING,
    allowNull: false,
  },
  price: {
    type: DataTypes.FLOAT,
    allowNull: false,
  },
});


module.exports = Product;

// const products = [
//   {
//     id: 1,
//     name: "Apple",
//     price: 0.5,
//   },
// ];

// const getProducts = () => products;

// const addProduct = (product) => {
//   products.push(product);
// };

// const updateProduct = (id, updatedProduct) => {
//   const index = products.findIndex((product) => product.id === id);
//   if (index !== -1) {
//     products[index] = updatedProduct;
//     return true;
//   }
//   return false;
// };

// const deleteProduct = (id) => {
//   const index = products.findIndex((product) => product.id === id);
//   if (index !== -1) {
//     products.splice(index, 1);
//     return true;
//   }
//   return false;
// };

// module.exports = {
//   getProducts,
//   addProduct,
//   updateProduct,
//   deleteProduct,
// };




