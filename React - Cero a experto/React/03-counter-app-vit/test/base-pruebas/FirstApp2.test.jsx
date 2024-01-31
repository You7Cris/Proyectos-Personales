import { render, screen } from '@testing-library/react';
import { FirstApp } from '../../src/FirstApp';

describe('Pruebas en < FirstApp />', () => {

  const title = "Hola, Soy Goku";
  const subTitle = "Soy un subtitulo";

  test('debe de hacer math con el snapshot', () => {
    
    const { container } = render( <FirstApp title={ title } />);
    expect( container ).toMatchSnapshot();
  });

  test('debe de mostrar el mensaje "Hola, Soy Goku" ', () => {

    
    render( <FirstApp title={ title } />);
    // screen.debug();
    expect( screen.getByText(title) ).toBeTruthy();

  });

  test('debe de mostrar el titulo en un h1', () => {
    render( <FirstApp title={ title } />);
    expect( screen.getAllByRole('heading', { level: 1}).innerHTML ).toContain( title );
  });

  test('debe de mostrar el subtitulo enviado por props', () => {

    render( <FirstApp title={ title } subtitle={ subTitle } />);

    expect( screen.getAllByText(subtitle).length).toBe(2);
    
  })
  
  
  
  
  
  
  
});
