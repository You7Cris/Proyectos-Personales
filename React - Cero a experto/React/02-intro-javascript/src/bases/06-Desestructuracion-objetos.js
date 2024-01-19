// Desestructuracion
// Asignacion Desestructurante

const persona = {
    nombre: 'Cristian',
    edad: 24,
    clave: 'Ironman',
    rango : 'Soldado',
};

const { edad, clave, nombre,  } = persona;

// console.log( nombre );
// console.log( edad );
// console.log( clave );


// console.log( persona.nombre );
// console.log( persona.edad );
// console.log( persona.clave );

const perContext = ({clave, nombre, edad, rango = 'Capitan' }) => {

    //const { edad, clave, nombre, } = usuario;
    //console.log(usuario);

    //console.log( edad, clave, nombre)
    //console.log( nombre, edad, rango );
    return {
        nombreClave: clave,
        anios: edad,
        latlng: {
            lat: 14.1232,
            lng: -12.3232
        }
    }
}

const { nombreClave, anios, latlng:{lat, lng} } = perContext( persona );

console.log(nombreClave, anios);
console.log( lat, lng );