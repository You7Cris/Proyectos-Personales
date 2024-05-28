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
    mysql:{
        host: process.env.DB_HOST || 'localhost',
        user: process.env.DB_USER || 'root',
        passwd: process.env.DB_PASS || '',
        database: process.env.DB || 'db_asignacion_juegos',
    }

    //continua en mysql.js
}

//Paso 2
//mediante la consolña de comandos se ingresa a la carpeta del proyecto y desde allio se instalan
// express, nodemon y dotenv -D
//Continua en app.js