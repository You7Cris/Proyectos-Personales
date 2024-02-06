import { renderHook, waitFor } from '@testing-library/react';
import { useFetchGifs } from "../../src/hooks/useFetchGifs";

describe('Pruebas en el hook useFecthGifs', () => {
    test('debe de regresar el estado inicial', () => {

        //const { images, isLoading } = useFetchGifs();

        const { result } = renderHook( () => useFetchGifs('One Punch'));
        const { images, isLoading } = result.current;
        //console.log(result);

        expect( images.length ).toBe(0);
        expect( isLoading ).toBeTruthy();
      
    });

    test('debe de retornar un arreglo de imagenes y el isLoading en false', async() => {

        //const { images, isLoading } = useFetchGifs();

        const { result } = renderHook( () => useFetchGifs('One Punch'));

        await waitFor(
            () => expect( result.current.images.length ).toBeGreaterThan(0)
        );
        const { images, isLoading } = result.current;

        expect( images.length ).toBeGreaterThan(0);
        expect( isLoading ).toBeFalsy();
      
    });
    
})
