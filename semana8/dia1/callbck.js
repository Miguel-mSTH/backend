function hola(nombre, micallback) {
  setTimeout(function () {
    console.log("Hola " + nombre);
    micallback(nombre);
  }, 1000);
}

function hablar(nombre, segundocallback) {
  setTimeout(function () {
    console.log("Como te va " + nombre);
    segundocallback(nombre);
  }, 1000);
}

function adios(nombre, tercercallback) {
  setTimeout(() => {
    console.log("Adios " + nombre);
    tercercallback();
  }, 1000);
}

/* hola("Miguel", function (nombre) {
    console.log("Adios " + nombre);
  });
   */
hola("Miguel", function (nombre) {
  hablar(nombre, function (nombre) {
    adios(nombre, function () {
      console.log("fin...");
    });
  });
});
