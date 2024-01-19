const persona = {
    nombre: 'Cristian',
    apellido: 'Gonzalez',
    edad: 24,
    direccion: {
        ciudad: 'Cartago',
        zip: 7600201,
        lat: 14.3234,
        lng: 34.923321
    }
};

//console.table( persona );
//console.log( { persona: persona });
//console.log( persona );

//const persona2 = persona;
const persona2 = { ...persona };
persona2.nombre = 'Steven';

console.log( persona );
console.log(persona2);