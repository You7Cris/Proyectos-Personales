

//Quitar any, mala practica

export function whatsMyType<T>( argument: T ): T { //Generico T, toma el argumento del tipo T y lo devuelve igual
    return argument;
}

const amIString = whatsMyType<string>('Hola Mundo');
const amINumber = whatsMyType<number>(100);
const amIArray = whatsMyType<number[]>([1,2,3,4,5]);

console.log(amIString.split('')); 
console.log(amINumber.toFixed());
console.log(amIArray.join('-'));