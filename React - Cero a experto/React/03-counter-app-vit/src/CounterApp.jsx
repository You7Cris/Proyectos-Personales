import { useState } from 'react'; // esto es un Hook
import PropTypes from 'prop-types'

export const CounterApp = ( {value} ) => {

    console.log('render');
    // API....FETCH.......

    const [ counter, setCounter ] = useState( value );

    const hanleAdd = () => { 
        //console.log(event)
        //console.log(newValue)
        //counter++;
        setCounter( counter + 1 );
        //setCounter( (c) => c + 1 )
    }

    // const restAdd = () => {
    //     setCounter( counter - 1 );
    // }

    //const handleSubstract = () => setCounter( counter - 1);
    //const handleReset = () => setCounter( value );
    const restAdd = () => setCounter( counter - 1);
    const resetAdd = () => setCounter( value );

    // const resetAdd = () => {
    //     setCounter( value );
    // }
    

    return (
        <>
            <h1>CounterApp</h1>
            <h2> { counter } </h2>

            <button onClick={ hanleAdd }> +1 </button>
            <button onClick={ restAdd }> -1 </button>
            <button onClick={ resetAdd }> Reset </button>
        </>
    );
}

CounterApp.propTypes = {
    value: PropTypes.number.isRequired,
}