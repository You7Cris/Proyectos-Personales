// async 

// const getImagenPromesa = () => new Promise( resolve => resolve('https://ajskdhasjdhajs.com'))

// getImagenPromesa().then( console.log );

const getImage = async() => {

    try {
        const apiKey = 'Apg1jS8ujT1O4qzyFV0gd1ICCAZro8SC';
        const resp = await fetch(`https://api.giphy.com/v1/gifs/random?api_key=${ apiKey }`);
        const  { data } = await resp.json();
        console.log(data);
        const { url } = await data.images.original;
        const img = document.createElement('img')
        img.src = url;
        document.body.append( img );
    } catch (error) {
        // Manejo del error
        console.error(error);
        
    }
    

}
           

getImage();
//console.log( getImage() );
//getImage().then( console.log )
    