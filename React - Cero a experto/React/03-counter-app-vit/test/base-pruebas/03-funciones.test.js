import { getUser, getUsuarioActivo } from '../../src/base-pruebas/05-funciones';


describe('Pruebas en 05-funciones', () => {
    test('getUser debe retornar un objeto', () => {

        const testUser = {
            uid: 'ABC123',
            username: 'El_Papi1502'
        };

        const user = getUser();
        //console.log(user);

        //expect( testUser ).toBe( user ); //Cuando son dos objetos estan apuntando a valores de memoria diferentes.
        expect( testUser ).toEqual( user );
    });

    test('getUsuarioActivo debe de retornar un objeto', () => {

        const name = 'Fernando';

        // const testUserActive = {
        //     uid: 'ABC567',
        //     username: name
        // }
        const userActive = getUsuarioActivo(name);

        //console.log(user);

        expect( userActive ).toStrictEqual({
            uid: 'ABC567',
            username: name
        });

    })
});