const db = require('../../db/mysql');

const TABLA = 'juegos'

function obtenerJuegos(){
    return db.obtenerDatos(TABLA);
}

function obtenerRegJuego(id){
    return db.obtenerRegistro(TABLA, id, 'cod_juego');
}

function agregarRegJuego(data){
    return db.agregarRegistro(TABLA, data);
}

function eliminarRegJuego(id){
    return db.eliminarRegistro(TABLA, id, 'cod_juego');
}

function actualizarRegJuego(data){
    return db.actualizarRegistro(TABLA, data, 'cod_juego');
}

//Paso 36
//Se exportan las funciones para su uso en la app

module.exports = {
    obtenerJuegos,
    obtenerRegJuego,
    agregarRegJuego,
    eliminarRegJuego,
    actualizarRegJuego,
}

//Continua en rutas.js