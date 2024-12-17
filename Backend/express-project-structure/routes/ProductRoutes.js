const express = require("express");
const ProductController = require('../controllers/productsController');

const router = express.Router();

router.post("/products", ProductController.createProducts );


router.get("/products",ProductController.getProducts);


router.delete("/products/:id", ProductController.deleteProduct);


router.put("/products/:id", ProductController.updateProduct );

module.exports=router;
