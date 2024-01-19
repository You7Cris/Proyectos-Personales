// Funciones en JS

const saludar = function( nombre ){
    return `Hola, ${ nombre }`;
}

//saludar = 30;

const saludar2 = ( nombre ) => {
    return `Hola, ${ nombre }`;
}

const saludar3 = ( nombre ) =>  `Hola, ${ nombre }`;
const saludar4 = () => `Hola Mundo`;

//console.log( saludar('Cristian') );

console.log( saludar );
console.log( saludar2('Cristian'));
console.log( saludar3('Goku'));
console.log( saludar4() );

// const getUser = () => {
//     return {
//         uid: 'ABC123',
//         username: 'El_Papi1502'
//     }
// }

const getUser = () => ({
        uid: 'ABC123',
        username: 'El_Papi1502'
    }
);

const user = getUser();
console.log(user);

console.log( getUser() );

// Tarea
// 1. Transformar la funcion en flecha
// 2. Tiene que retornar objeto implicito
// 3. Prueba

function getUsuarioActivo( nombre ) {
    return {
        uid: 'ABC567',
        username: nombre
    }
}

const usuarioActivo = ( nombre ) => ({
    uid: 'ABC567',
    nombre : nombre
});

//const usuarioActivo = getUsuarioActivo('Cristian');
console.log( usuarioActivo('Cristian') );
 