import { render, screen } from "react-dom"
import { GifExpertApp } from "../src/GifExpertApp"

describe('Pruebas en <GifExpertApp />', () => {

    test('Pruebas en el onaddCategory', () => {

        render( <GifExpertApp />);
        screen.debug()
      
    })
    
  
})
