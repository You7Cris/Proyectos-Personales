// Paso 3
const express = require('express');
const config = require('./config');

const app = express();
app.set('port', config.app.port);

// Paso 20
// Cargo en la app las rutas para los servicios o modulos de la app
// const gestion_juego = require('./modulos/gestion_juegos/rutas');
const gestion_juego = require('./modulos/gestion_juegos/rutas');
const gestion_genero = require('./modulos/gestion_generos/rutas');
const gestion_grupo = require('./modulos/gestion_grupos/rutas');


// Paso 21
// Creo las rutas a los diferentes servicios o modulos de la app
app.use('/api/gestion_juego', gestion_juego);
app.use('/api/gestion_genero', gestion_genero);
app.use('/api/gestion_grupo', gestion_grupo);

// Paso 22
//localhost:4000/api/gestion_juego

// Paso 6
module.exports = app;
