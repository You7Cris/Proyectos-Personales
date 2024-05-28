// Paso 3
const express = require('express');
const config = require('./config');
const cors = require('cors'); //Paso 41

const app = express();


//Paso 40
//Middleware: 
app.use(express.json()); // Se utiliza para poder recibir y enviar JSON en las peticiones 
app.use(express.urlencoded({ extended: true})); //true: utiliza la biblioteca "qs" para analizar 
//Manejar //los datos codificados en URL. Esta puede manejar objetos y arrays anidados. Con false usa la "querystring" que no los soporta. Solo puede manejar pares de clave-valor planos.

//Paso 42
// Se agrega "cors" al middleware:
app.use(cors());

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
