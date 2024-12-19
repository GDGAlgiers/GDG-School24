const products = [
  {
    id: 1,
    name: "Apple",
    price: 0.5,
  },
];

const addToProducts = (product) => {
  products.push(product);
};

const getProducts = () => {
  return products;
};

const deleteProductById = (id) => {
  const index = products.findIndex((product) => product.id == id);
  if (index != -1) {
    products.splice(index, 1);
    return true;
  }
  return false;
};

const updateProductById = (id, updatedProduct) => {
  const index = products.findIndex((product) => product.id == id);
  if (index != -1) {
    products[index] = updatedProduct;
    return true;
  }
  return false;
};

module.exports = {
  addToProducts,
  getProducts,
  deleteProductById,
  updateProductById,
};