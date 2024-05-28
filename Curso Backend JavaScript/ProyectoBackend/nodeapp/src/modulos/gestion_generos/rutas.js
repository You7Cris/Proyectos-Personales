// Paso 15
// Llamo a el framework Express 
const express = require('express');

//Paso 16
// creacion de rutas
const router = express.Router();

//Paso 17
// Crea las rutas a las acciones de prueba del servicio

//Rutas de prueba
// La ruta 'home' es la ruta por defecto que se accedera cuando se llame el servicio "gestion_juegos"

router.get('/', home);

router.get('/alterna', functionAlterna);


//Paso 18
// Funciones para las acciones de prueba

async function home(req, resp){
    resp.send('Llamada exitoso a la accion "Home" del servicio gestion_juegos');
}


async function functionAlterna(req, resp){
    resp.send('Llamada exitoso a la accion "Alterna" del servicio gestion_juegos');
}

//Paso 19
// Exporto a router para poder usarlo en el resto 
module.exports = router;