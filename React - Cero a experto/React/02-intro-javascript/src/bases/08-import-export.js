// import { heroes } from './data/heroes'

//import { heroes } from './data/heroes'
// import heroes, {owners} from './data/heroes';
//import { heroes, owners } from './data/heroes';
import heroes, {owners} from "../data/heroes";

console.log(owners);
console.log( heroes );

// const getHeroeById = (id) => {
//     //return {};
//     return heroes.find(( heroe ) => {
//         if (heroe.id == id) {
//             return true;
//         }else{
//             return false;
//         }
        
//     });
// }

// const getHeroeById = (id) => {
//     //return {};
//     return heroes.find(( heroe ) => heroe.id == id);
// }

const getHeroeById = (id) => heroes.find( ( heroe ) => heroe.id == id);

console.log( getHeroeById(1) );

// find, filter
const getHeroeByOwner = ( owner ) => heroes.filter( (heroe) => heroe.owner == owner);

console.log( getHeroeByOwner('DC'));