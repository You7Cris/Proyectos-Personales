import PropTypes from 'prop-types';

import { GifItem } from "./GifItem";
import { useFetchGifs } from "../hooks/useFetchGifs";
//import { getGifs } from "../helpers/getGifs";



export const GifGrid = ({ category }) => {

    const { images, isLoading} = useFetchGifs( category );

    //console.log(isLoading);


    //getGifs(category);

    return (
        <>
            <h3>{ category }</h3>
            {
                isLoading && ( <h2>Cargando...</h2>)
            }
            <div className="card-grid">
                {/* images.map()... */}
                {
                    images.map( ( image ) => (
                        <GifItem key={ image.id } 
                        {
                            ...image
                        }
                        // title = { image.title }
                        // url = { image.url }
                        />
                    ))
                }
            </div>
           
        </>
    )
}


category.propTypes = {
    category: PropTypes.string.isRequired,
}

