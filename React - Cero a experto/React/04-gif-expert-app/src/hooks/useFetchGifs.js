import { useState, useEffect } from 'react';
import { getGifs } from '../helpers/getGifs';


// un Hook es una funcion que regresa algo 
export const useFetchGifs = ( category ) => {

    const [images, setImages] = useState([]);
    const [isLoading, setIsLoading] = useState(true);

    const getImages = async() => {
        const newImages = await getGifs( category );
        setImages(newImages);
        setIsLoading(false);
    }
    
    // useEffect permite disparar un efecto secundario 
    useEffect( () => {
    //    getGifs(category)
    //    .then( newImages => setImages(newImages) );
        getImages();
    }, [])

    return {
        images,
        isLoading
    }
}

