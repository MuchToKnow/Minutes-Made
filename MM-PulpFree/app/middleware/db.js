const { Pool } = require("pg");

const pool = new Pool({
  user: "app",
  host: "minutes-made.cvt0ckrxsc9j.us-east-2.rds.amazonaws.com",
  database: "Minutes",
  password: "oZqs94JrzUTwc5l5hcA5",
  port: 5432
});

module.exports = {
  pool
};
