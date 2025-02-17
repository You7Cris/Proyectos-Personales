alert("Hola mundo");

var nombre = "Cristian Gonzalez";
var altura = 179;
var edad = 25;

var concatenacion = nombre + " " + altura;

// document.write(nombre);
// document.write(altura);
// var datos = document.getElementById("datos");
// datos.innerHTML = `
//     <h1>Soy la caja de datos</h1>
//     <h2>Mi nombre es: ${nombre}</h2>
//     <h3>Mi altura es: ${altura}</h3>
// `;

if (altura >= 190) {
    datos.innerHTML += `<h4>Eres una persona alto</h4>`;
} else {
    datos.innerHTML += `<h4>Eres una persona baja</h4>`;
}

for (var i = 2000; i <= 2020; i++) {
    //bloque de instrucciones
    datos.innerHTML += `<h2>Estamos en el Año ${i}</h2>`;
}
// document.getElementById(nombre).innerHTML = nombre;

function MuestraMiNombre(nombre, altura) {
    var misDatos = `
    <h1>Soy la caja de datos</h1>
    <h2>Mi nombre es: ${nombre}</h2>
    <h3>Mi altura es: ${altura}</h3>
    `;

    return misDatos
}

function imprimir() {
    var datos = document.getElementById("datos");
    datos.innerHTML = MuestraMiNombre("Cristian Gonzalez", 179);
}

imprimir();

var nombres = ["Cristian", "Victor", "Daniela", "Andres"];
alert(nombres[0]);

// for (var i = 0; i < nombres.length; i++) {
//    document.write(nombres[i] + '<br>');
// }

nombres.forEach((nombre) => {
    document.write(nombre + '<br>');
});