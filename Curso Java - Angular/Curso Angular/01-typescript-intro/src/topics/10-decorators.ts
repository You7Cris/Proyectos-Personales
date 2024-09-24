// function classDecorator<T extends { new (...args:any[]):{} }>(
//     constructor: T
// ){

// }

function classDecorator<T extends { new (...args:any[]):{} }>(
    constructor: T
){
    return class extends constructor{
        newProperty = 'New Property';
        hello = 'override';
    }
}


@classDecorator //Añade o cambia el comportamiento de nuestra clase
export class SuperClass {

    public myProperty: string = 'Abcd123';

    print() {
        console.log('Hola mundo');
    }

}

console.log(SuperClass);

const myClass = new SuperClass();
console.log(myClass);