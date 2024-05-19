// Paso 15
// Llamo a el framework Express 
const express = require('express');

//Paso 27
// Carga el archivo con las respuestas estandarizadas
const respuesta = require('../../controladores/respuestas');

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
    // resp.send('Llamada exitoso a la accion "Home" del servicio gestion_juegos');
    
     //Paso 28
    // Se implementan las nuevas respuestas de exito y error
    try{
        respuesta.sucess(req, resp, 'Llamada exitoso a la accion Home del servicio Gestion_Juegos', 200);
    }catch(err){
        respuesta.error(req, resp, 'Error interno del servidor' + err, 500);
    }
   
}


async function functionAlterna(req, resp){
    // resp.send('Llamada exitoso a la accion "Alterna" del servicio gestion_juegos');
    try{
        respuesta.sucess(req, resp, 'Llamada exitoso a la accion Alterna del servicio Gestion_Juegos', 200);
    }catch(err){
        respuesta.error(req, resp, 'Error interno del servidor' + err, 500);
    }
}

//Paso 19
// Exporto a router para poder usarlo en el resto 
module.exports = router;