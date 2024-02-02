import React, { useState } from 'react';
import { AddCategory, GifGrid } from './components';

export const GifExpertApp = () => {

    const [categories, setCategories] = useState([ 'One Punch' ]);

    // console.log(categories);
    const onAddCategory = (newCategory) => {
        console.log(newCategory);

        if ( categories.includes(newCategory) ) return;
        //categories.push(newCategory);
        // categories.push('Valorant');
        // setCategories( [ ...categories, 'Valorant' ]);
        //setCategories( cat => [...cat, 'Valorant']);
        setCategories( [ newCategory, ...categories]);
    }

    return (
        <>
            <h1>GifExpertApp</h1>
            <AddCategory 
                //setCategories={ setCategories }
                onNewCategory={ (value) => onAddCategory(value)}
                //currentCategories={ categories }
            />
            {/* Listado de items (Gifs) */}
           
            { 
                categories.map( ( category ) => 
                    (
                        <GifGrid 
                            key={ category } 
                            category={ category } />
                )) 
            }
            {/* <li>ABC</li> */}
            
            {/* Gif Item */}
        </>
    )
}