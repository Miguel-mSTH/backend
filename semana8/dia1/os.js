// trabajando con el sitema operativo
const os = require("os");

console.log(os.arch());
console.log(os.platform());
console.log(os.cpus().length);
console.log(os.totalmem());

const tam = 1024;
function kb(bytes) {
  return bytes / tam;
}
function mb(bytes) {
  return kb(bytes) / tam;
}
function gb(bytes) {
  return mb(bytes) / tam;
}
console.log("memoria ram en gb " + gb(os.totalmem()));
