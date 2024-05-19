//Paso 25
// Se carga a dotenv para manejar las variables de entorno y asi poder utilizar el valor de "process.env.PORT" del atributo "port"

require('dotenv').config();


module.exports = {

    //Paso 1 
    // Se crea el atributo "port" para definirr el puerto por el que se podra realizar la conexion a la app

    app:{
        port: process.env.PORT || 4000,
    },

    //Paso 30 se configuran los atributos requeridos para la conexion con la BD
}

//Paso 2