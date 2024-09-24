export class Person {
    // public name: string;
    // private address: string;

    constructor(
        public name: string, 
        public lastname: string,
        private address: string = 'No Address',
        // public address?: string
        ) 
        {}

    //Funciones dentro de las clases son metodos
}

// export class Hero extends Person{


//     constructor(
//         public alterEgo: string,
//         public age: number,
//         public realName: string,
//     ) {
//         super(realName, 'Cartago');
//     }
// }

export class Hero{

    // public person: Person;

    constructor(
        public alterEgo: string,
        public age: number,
        public realName: string,
        public person: Person,
    ) {
        // this.person = new Person(realName);
    }
}

//Inyeccion de dependencias se va a realizar en el constructor
const tony = new Person('Tony Stark','New York');
const ironman = new Hero('Ironamn', 45, 'Tony Stark', tony);

console.log(ironman);

