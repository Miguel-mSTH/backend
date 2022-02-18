const os = require("os");
const factor = 1024;
async function memoria(bytes) {
  return new Promise(function (resolve, reject) {
    result = bytes / factor;
    resolve(result);
  });
}

async function main() {
  kb = await memoria(os.totalmem());
  mb = await memoria(kb / 1024);
  //console.log("KB: " + mb);
  console.table([
    { capacidad: "KB", tam: kb },
    { capacidad: "MB", tam: mb },
  ]);
}

main();
