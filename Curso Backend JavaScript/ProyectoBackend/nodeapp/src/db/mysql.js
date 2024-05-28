// Paso 29
// Se carga el modulo de manejo de la bd y el archivo que contiene la info de configuracion
const mysql = require('mysql');
const config = require('../config');

//Paso 31
// Se crea el objeto de configuracion de MySQL con los valores traidos de config.js
const dbconfig = {
    host: config.mysql.host,
    user: config.mysql.user,
    passwd: config.mysql.passwd,
    database: config.mysql.database,
};

//----------------------
// Paso 32
// Se configura e inicia la conexion a la bd

// Se crea la variable de conexion

var conexion;

// Se crea la funcion mediante la que se iniciara la conexion 
function conectarBD(){

    conexion = mysql.createConnection(dbconfig);

    conexion.connect((err) => {
        if(err){
            console.log("Error en la conexion con la BD: " + err.message);
            setTimeout(conectarBD, 200); // Intenta reconextar en 200 ms si hay error
        }else{
            console.log("Conexion exitosa a la BD");
        }
    });

    conexion.on('error', (err) => {
        console.log("Se ha perdido la conexion a MySQL: " + err.message);

        if(err.code === 'PROTOCOL_CONNECTION_LOST') {
            conectarBD();
        }else{
            throw err; //Algo esta mal con la BD
        }
    });
}

// Se inicia la conexion
conectarBD();


// Traer los datos de una tabla
function obtenerDatos(tabla){
    return new Promise((resolve, reject) => {
            conexion.query(`SELECT * FROM ${tabla}`, (err, result) => {
                return !err ? resolve(result) : reject(console.log('Algo salio mal al realizar la consulta: ${err}'));
            });
        });
}

// Traer un registro de una tabla
function obtenerRegistro(tabla, id, codigo){
    return new Promise((resolve, reject) => {
        conexion.query(`SELECT * FROM ${tabla} WHERE ${codigo} = ${id}`, (err, result) => {
                    return !err ? resolve(result) : reject(console.log('Algo salio mal al realizar la consulta: ${err}'));
                });
    });

}


//Agregar un registro a una tabla
function agregarRegistro(tabla, data){
    return new Promise((resolve, reject) => {
            conexion.query(`INSERT INTO ${tabla} SET ?`, data, (err, result) => {
                        return !err ? resolve(result) : reject(console.log('Algo salio mal al realizar la creacion: ${err}'));
                    });
        });
}


//Elimina un registro de una tabla
function eliminarRegistro(tabla, id, codigo){
    return new Promise((resolve, reject) => {
                conexion.query(`DELETE FROM ${tabla} WHERE ${codigo} = ${id}`, (err, result) => {
                            return !err ? resolve(result) : reject(console.log('Algo salio mal al realizar la eliminacion: ${err}'));
                        });
            });
}

//Actualizar un registro en una tabla
// function actualizarRegistro(tabla, data, codigo){
//     return new Promise((resolve, reject) => {
//                     conexion.query(`UPDATE ${tabla} SET ? WHERE ${codigo} = ?`, [data, eval(`data.${codigo}`)] , (err, result) => {
//                                 return !err ? resolve(result) : reject(console.log(`Algo salio mal al realizar la actualizacion: + data.${codigo} + ${err}`));
//                     });
//             });
// }

function actualizarRegistro(tabla, data, codigo) {
    return new Promise((resolve, reject) => {
        conexion.query(`UPDATE ${tabla} SET ? WHERE ${codigo} = ?`, [data, eval(`data.${codigo}`)], (err, result) => {
            return !err ? resolve(result) : reject(console.log(`Algo salio mal al realizar la actualizacion: + data.${codigo} + ${err}`));
        });

    // return new Promise((resolve, reject) => {
    //         const query = `UPDATE ?? SET ? WHERE ?? = ?`;
    //         const values = [tabla, data, codigo, data[id]];

    //         conexion.query(query, values, (err, result) => {
    //             return !err? resolve(result) : reject(console.log(`Algo salio mal al realizar la actualizacion: + data.${codigo} + ${err}`));
    //         });
    // });
    });
}

// Promise: El constructor de Promise recibe dos paramteros: resolve y reject, que son dos funciones de devolucion

// de llamada (callback).


module.exports = {
    obtenerDatos,
    obtenerRegistro,
    agregarRegistro,
    eliminarRegistro,
    actualizarRegistro,
}