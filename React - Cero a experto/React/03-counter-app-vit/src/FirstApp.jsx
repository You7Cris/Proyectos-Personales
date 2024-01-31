//import { Fragment } from 'react';

//const newMessage = 'Cristian';
//const newMessage = [1,2,3,4,5,6,7,8,9];
// const newMessage = {
//     message: 'Hola Mundo',
//     title: 'Cristian'
// };

// Async daria error
// const getResult = (a, b) => {
//     return a + b;
// }

import PropTypes from 'prop-types';



// props -> propiedades que le estamos mandando a la funcion
export const FirstApp = ( /*props*/ { title, subtitle, name } ) => {

    //console.log(props);
    // if ( !title ) {
    //     throw new Error('El titulo no existe');
    // }

    return (
        <>
        {/* <div> */}
            {/* <h1>{ newMessage }</h1> */}
            {/* <h1>{ JSON.stringify(newMessage) }</h1> */}
            {/* <h1>{ getResult(5, 9) }</h1> */}
            {/* <h1>{ title }</h1> */}
            <h1 data-testid="test-title">{ title }</h1>
            <p>{ subtitle }</p>
            <h1>{ subtitle }</h1>
            <p>{ name }</p>
            {/* <p>Soy un subtitulo</p> */}
        {/* </div> */}
        </>

    )
    
}

FirstApp.propTypes = {
    title: PropTypes.string.isRequired,
    subtitle: PropTypes.string.isRequired,
}

FirstApp.defaultProps = {
    //title: 'No hay titulo',
    subtitle: 'No hay subtitulo' ,
    name: 'Cristian Gonzalez',
}