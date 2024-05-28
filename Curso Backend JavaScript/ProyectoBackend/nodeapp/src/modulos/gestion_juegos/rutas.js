// Paso 15
// Llamo a el framework Express 
const express = require('express');

//Paso 27
// Carga el archivo con las respuestas estandarizadas
const respuesta = require('../../controladores/respuestas');

//Paso 37
//Se carga el archivo controlador de la bd para utilizar las funciones
const controlador_db = require('./controlador_db');

//Paso 16
// creacion de rutas
const router = express.Router();

//Paso 17
// Crea las rutas a las acciones de prueba del servicio

//Rutas de prueba
// La ruta 'home' es la ruta por defecto que se accedera cuando se llame el servicio "gestion_juegos"

router.get('/', home);

router.get('/alterna', functionAlterna);


//Paso 38
// Se crean las rutas validas para las diferentes acciones del servicio
router.get('/consultar', obtenerJuegos);
router.get('/consultar/:id', obtenerRegJuego);
router.post('/crear', agregarRegJuego);
router.delete('/eliminar/:id', eliminarRegJuego);
router.put('/actualizar', actualizarRegJuego);


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

//Paso 39
// Se crean las funciones para cada accion llamada por cada ruta

async function obtenerJuegos(req, res){
    try{
        const items = await controlador_db.obtenerJuegos();
        respuesta.sucess(req, res, items, 200);
    }catch(err){
        respuesta.error(req, res, 'Error interno del servidor' + err, 500);
    }
};

async function obtenerRegJuego(req, res){
    try{
            const items = await controlador_db.obtenerRegJuego(req.params.id);
            respuesta.sucess(req, res, items, 200);
        }catch(err){
            respuesta.error(req, res, 'Error interno del servidor' + err, 500);
        }
};

async function agregarRegJuego(req, res){
    try{
        const items = await controlador_db.agregarRegJuego(req.body);
        respuesta.sucess(req, res, items, 200);
    }catch(err){
        respuesta.error(req, res, 'Error interno del servidor' + err, 500);
    }
};

async function eliminarRegJuego(req, res){
    try{
        const items = await controlador_db.eliminarRegJuego(req.params.id);
        respuesta.sucess(req, res, items, 200);
    }catch(err){
        respuesta.error(req, res, 'Error interno del servidor' + err, 500);
    }
};

async function actualizarRegJuego(req, res){
    const existe = await controlador_db.obtenerRegJuego(req.body.cod_juego);

    if(existe == ''){
        respuesta.sucess(req, res, 'Registro no existe', 201);
    }else{
        try{
            const items = await controlador_db.actualizarRegJuego(req.body);
            respuesta.sucess(req, res, 'Registro actualizado con exito', 201);
        }catch(err){
            respuesta.error(req, res, 'Error interno del servidor' + err, 500);
        }
    }
}

//Paso 19
// Exporto a router para poder usarlo en el resto 
module.exports = router;