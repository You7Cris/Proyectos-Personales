import { getImagen } from "../../src/base-pruebas/11-async-await"


describe('Pruebas en 11-async-await.js', () => {

    test('getImagen debe de retornar un URL de la imagen', async() => {

        const resp = await getImagen();
        //console.log(url);

        //expect( typeof url ).toBe('string');
        expect( typeof resp ).toBe('No se encontro la imagen');

      
    });
    
  
})
