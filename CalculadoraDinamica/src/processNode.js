function processNode(node) {

    const { operation, params } = node;

    if(!operation || !Array.isArray(params) || params.length === 0) {
        throw new Error('El nodo no es válido');
    }

    if(!params.every(parametro => typeof parametro === 'number')) {
        throw new Error('Los parámetros no son números');
    }

    let resultado;

    switch(operation) {
        case 'add':
            resultado = params.reduce((acum, valor) => acum + valor, 0);
            break;
        case 'subtract':
            resultado = params.slice(1).reduce((acum, valor) => acum - valor, params[0]); //se selecciona el primer parametro
            break;
        case 'multiply':
            resultado = params.reduce((acum, valor) => acum * valor, 1);
            break;
        case 'divide':
            resultado = params.slice(1).reduce((acum, valor) => {
                if (valor === 0) {
                    throw new Error('No se puede dividir por 0');
                }
                return acum / valor;
            }, params[0]);
            break;
        case 'sqrt':
            if(params.length !== 1) {
                throw new Error('La operación sqrt solo acepta 1 parámetros');
            }
            resultado = Math.sqrt(params[0]);
            break;
        case 'power':
            if(params.length !== 2) {
                throw new Error('La operación power solo acepta 2 parámetros');
            }
            resultado = Math.pow(params[0], params[1]);
            break;
        default:
            throw new Error('Operación no soportada');
    }

    return { ...node, response: resultado };
}

module.exports = { processNode };