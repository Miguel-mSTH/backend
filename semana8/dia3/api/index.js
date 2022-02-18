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
    content: "Bienvenido a mi API Students",
  });
});

const mysqlConnection = require("./database");
app.get("/alumnos", function (req, res) {
  mysqlConnection.query("select * from tbl_alumno", (err, rows, fields) => {
    if (!err) {
      res.json(rows);
    } else {
      console.log(err);
    }
  });
});

app.post("/alumnos", function (req, res) {
  const { alumno_id, alumno_nombre, alumno_email } = req.body;
  const query =
    "insert into tbl_alumno (alumno_id,alumno_nombre,alumno_email) values(?,?,?)";

  mysqlConnection.query(
    query,
    [alumno_id, alumno_nombre, alumno_email],
    (err, rows, fields) => {
      if (!err) {
        res.json({
          status: true,
          content: "students inserted",
        });
      } else {
        console.log(err);
      }
    }
  );
});

app.put("/alumnos/:alumno_id", function (req, res) {
  const { alumno_nombre, alumno_email } = req.body;
  const { alumno_id } = req.params;
  const query =
    "update tbl_alumno set alumno_nombre=?,alumno_email=? where alumno_id=?";

  mysqlConnection.query(
    query,
    [alumno_nombre, alumno_email, alumno_id],
    (err, rows, fields) => {
      if (!err) {
        res.json({
          status: true,
          content: "Student Updated",
        });
      } else {
        console.log(err);
      }
    }
  );
});

app.delete("/alumnos/:alumno_id", function (req, res) {
  const { alumno_id } = req.params;
  const query = "delete from tbl_alumno where alumno_id=?";

  mysqlConnection.query(query, [alumno_id], (err, rows, fields) => {
    if (!err) {
      res.json({
        status: true,
        content: "Student deleted",
      });
    } else {
      console.log(err);
    }
  });
});

app.listen(app.get("port"), () => {
  console.log(`Server running at http://localhost:${app.get("port")}`);
});
