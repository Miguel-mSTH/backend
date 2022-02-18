const express = require("express");

const app = express();

app.get("/", (req, res) => {
  res.send("<center><h1>HOLA MUNDO EXPRESS MIGUEL ESPINOZA</h1></center>");
});

app.get("/json", function (req, res) {
  res.json({
    nombre: "miguel espinoza",
    email: "miguel@gmail.com",
  });
});

app.get("/saludar/:nombre", function (req, res) {
  res.send("HOLA " + req.params.nombre);
});

app.get("/formulario", function (req, res) {
  html = "<form action='http://localhost:9000/saludopost' method='POST'>";
  html += "<input type='text' name='nombre'/>";
  html += "<input type='submit' name='saludar'/>";
  html += "</form>";
  res.send(html);
});

const bodyParser = require("body-parser");
app.use(bodyParser.urlencoded({ extended: true }));

app.post("/saludopost", function (req, res) {
  html = "<h1>HOlA COMO ESTAS " + req.body.nombre + "</h1>";
  res.send(html);
});

/////////utilizando json
app.use(express.json());

app.post("/saludopostjson", function (req, res) {
  const nombre = req.body.nombre;
  res.json({
    saludo: "hola " + nombre,
  });
});

app.listen(9000, function () {
  console.log("Servidor corriendo en http://localhost:9000");
});
