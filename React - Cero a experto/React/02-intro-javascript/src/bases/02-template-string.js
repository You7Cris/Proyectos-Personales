// Template Strings

const nombre = 'Cristian';
const apellido = 'Gonzalez';

//const nombreCompleto = nombre + ' ' + apellido;`
// `` = Alt Gr + }
const nombreCompleto = `${ nombre } ${ apellido }`;

console.log(nombreCompleto);

function getSaludo(nombre) {
    return ' Hola ' + nombre;
}

console.log( `Este es un texto: ${ getSaludo( nombre ) } `);