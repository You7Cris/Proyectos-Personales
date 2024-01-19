const personajes = ['Goku','Vegeta','Trunks'];

// console.log( personajes[0]);
// console.log( personajes[1]);
// console.log( personajes[2]);

const [ p1 ] = personajes; // goku
const [ , p2 ] = personajes; // Vegeta
const [ , , p3 ] = personajes // Trunks

console.log( p3 );

const retornaArreglo = () => {
    return ['ABC', 123];
}

const [ letras, numeros ] = retornaArreglo();
console.log(letras, numeros);

// Tarea
// 1. Primer valor del arr se llamara nombre
// 2. se llamara setNombre
const letState = ( valor ) => {
    return [ valor, () => {console.log('Hola Mundo') } ];

}

const [ nombre, letNombre ] = letState( 'Goku' );

console.log( nombre);
letNombre();
//arr[1]();