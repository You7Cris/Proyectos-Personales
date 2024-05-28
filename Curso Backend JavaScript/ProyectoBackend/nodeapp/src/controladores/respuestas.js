// Paso 26
// Se configura la respuesta de exito

exports.sucess = function (req, res, mensaje = 'Su solicitud fue recibida, entendida y aceptada con exito', status = 200) {

    res.status(status).send({
        error : false,
        status : status,
        body: mensaje
    });
}

// Se configura la respuesta de error 

exports.error = function (req, res, mensaje = 'Error', status = 500) {

    res.status(status).send({
        error : true,
        status : status,
        body: mensaje
    });
}