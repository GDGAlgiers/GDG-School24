const { Sequelize } = require('sequelize');

// Initialize Sequelize
const sequelize = new Sequelize({
  dialect: 'sqlite',
  storage: './config/app.db',
  logging: false, 
});

sequelize.sync();

module.exports = sequelize;
