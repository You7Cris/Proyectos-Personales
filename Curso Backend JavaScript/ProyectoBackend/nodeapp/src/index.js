
//Paso 7
// la instancia de la aplicacion

const app = require('./app');

//Paso 8
// Inicializamos el servidor 
// Con el listen escucha el puerto
// La funcion flecha para revisar que este bien

app.listen(app.get('port'), () => {
    console.log('Server on port', app.get('port'));
});