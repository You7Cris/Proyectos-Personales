import { getHeroeById } from "./bases/08-import-export";
import heroes from "./data/heroes";


// const promesa = new Promise( (resolve, reject) => {

//     setTimeout( () => {
//         // Tarea

//         //const heroe = getHeroeById(2);
//         //console.log( heroe );

//         //console.log('2 segundos despues');
//         //resolve( heroe );
//         const p1 = getHeroeById(2);
//         resolve( p1 );
//         //reject( 'No se pudo encontrar el heroe');
//     }, 2000)

// });

// promesa.then( (heroe) => {
//     //console.log('Then de la promesa');
//     console.log('heroe', heroe)
// })
// .catch( err => console.warn( err ));


const getHeroeByIdAsync = ( id ) => {

    const promesa = new Promise( (resolve, reject) => {

        setTimeout( () => {
            // Tarea
    
            //const heroe = getHeroeById(2);
            //console.log( heroe );
    
            //console.log('2 segundos despues');
            //resolve( heroe );
            const p1 = getHeroeById(id);
            console.log(p1);
            if( p1 ){
                resolve( p1 );
            }else{
                reject( 'No se encontro el heroe');
            }
            //resolve( p1 );
            //reject( 'No se pudo encontrar el heroe');
        }, 2000)
        
    });

    return promesa;

}

getHeroeByIdAsync(1)
    // .then( heroe => console.log('Heroe', heroe))
    .then( console.log )
    // catch ??
    //.catch( err => console.warn( err ));
    .catch( console.warn )
