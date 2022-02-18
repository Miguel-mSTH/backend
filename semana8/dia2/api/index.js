const express = require("express");
const app = express();
//

//settings
app.set("port", process.env.PORT || 9000);

//middlewares
app.use(express.json());

//Routes
app.get("/", (req, res) => {
  res.json({
    status: true,
    content: "Bienvenido a mi API",
  });
});

const mysqlConnection = require("./database");
app.get("/employee", function (req, res) {
  mysqlConnection.query("select * from employee", (err, rows, fields) => {
    if (!err) {
      res.json(rows);
    } else {
      console.log(err);
    }
  });
});

app.post("/employee", function (req, res) {
  const { name, salary } = req.body;
  const query = "insert into employee (name,salary) values(?,?)";

  mysqlConnection.query(query, [name, salary], (err, rows, fields) => {
    if (!err) {
      res.json({
        status: true,
        content: "employed inserted",
      });
    } else {
      console.log(err);
    }
  });
});

app.put("/employee/:id", function (req, res) {
  const { name, salary } = req.body;
  const { id } = req.params;
  const query = "update employee set name=?,salary=? where id=?";

  mysqlConnection.query(query, [name, salary, id], (err, rows, fields) => {
    if (!err) {
      res.json({
        status: true,
        content: "Employee Updated",
      });
    } else {
      console.log(err);
    }
  });
});

app.delete("/employee/:id", function (req, res) {
  const { id } = req.params;
  const query = "delete from employee where id=?";

  mysqlConnection.query(query, [id], (err, rows, fields) => {
    if (!err) {
      res.json({
        status: true,
        content: "Employee deleted",
      });
    } else {
      console.log(err);
    }
  });
});

app.listen(app.get("port"), () => {
  console.log(`Server running at http://localhost:${app.get("port")}`);
});

//create table employee (id int pk, name varchar(20), salary int(10));
