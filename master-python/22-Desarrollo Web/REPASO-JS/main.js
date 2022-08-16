//alert('Hola mundo');

var nombre = "Cristian Gonzalez";
var altura = 190;

/*
var concatenacion = nombre + " " + altura;

var datos = document.getElementById("datos");
datos.innerHTML = `
    <h1>Soy la caja de datos</h1>
    <h2>Mi nombre es: ${nombre}</h2>
    <h3>Mido: ${altura} cm</h3>
`;

//Comillas invetidas ```AlGr + z (<<) 

if(altura >= 190){
    datos.innerHTML += ` 
        <h1>Eres una persona ALTA</h1>
    `;
}else{
    datos.innerq += `
        <h1>Eres una persona BAJITA</h1>
    `;
}

for(var i=0; i<=2020; i++)
{
    //bloque de instrucciones
    datos.innerHTML += "<h2>Estamos en el año: " +i; 
}
*/

function MuestraMiNombre(nombre, altura){
    var misDatos = ` 
    <h1>Soy la caja de datos</h1>
    <h2>Mi nombre es: ${nombre}</h2>
    <h3>Mido: ${altura} cm</h3>
    `;

    return misDatos;
}

function imprimir(){
    var datos = document.getElementById("datos");
    datos.innerHTML = MuestraMiNombre("Cristian Gonzalez", 190);
}

imprimir();

var nombres = ['Cristian','Jhon','Joaquin']
//alert(nombres[0]);

document.write("<h1>Listado de nombres</h1>")
/*
for(i=0;i<nombres.length;i++)
{
    document.write(nombres[i] + "<br/>");
}
*/

nombres.forEach(function(nombre){
    document.write(nombre + '<br/>');
})

nombres.forEach((nombre) =>{
    document.write(nombre + '<br/>');
})
