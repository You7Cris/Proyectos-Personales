import { render } from '@testing-library/react';
import { FirstApp } from '../../src/FirstApp';

describe('Pruebas en < FirstApp />', () => {


  test('Debe de hacer match con el snapshot', () => {

    // const title = "Hola, Soy Goku";
    // const { container } = render( <FirstApp title={ title } /> )

    // console.log(container);

    // expect( container ).toMatchSnapshot();
    

    
  });

  test('debe de mostrar el titulo en un h1', () => {
    const title = "Hola, Soy Goku";
    const { container, getByText, getByTestId } = render( <FirstApp title={ title } /> )

    expect( getByText(title) ).toBeTruthy();

    // const h1 = container.querySelector('h1');
    // console.log(h1.innerHTML);

    // expect(h1.innerHTML).toBe( title )

    expect( getByTestId('test-title').innerHTML ).toContain(title);



  });

  test('debe mostrar el subtitulo enviado por props', () => {
    const title = "Hola, Soy Goku";
    const subtitle = "Hola, soy un subtitulo";
    const { getAllByText } = render( <FirstApp title={ title } subtitle={ subtitle } /> )

    expect( getAllByText(subtitle).length).toBe(2);
    expect( getAllByText(subtitle) ).toBeTruthy();
    
  });
  
  
  
});
