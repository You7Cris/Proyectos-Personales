import React from 'react' //imr importa directamente react
import ReactDOM  from 'react-dom/client'
import { HelloWorldApp } from './HelloWorldApp';
import { FirstApp } from './FirstApp';
//import { App } from './HelloWorldApp'
//import HelloWorldApp from './HelloWorldApp'

import './styles.css';
import { CounterApp } from './CounterApp';




ReactDOM.createRoot( document.getElementById('root')).render(
    <React.StrictMode>
        {/* <App /> */}
        {/* <HelloWorldApp /> */}
        {/* <FirstApp title = "Hola, Soy Cristian" subtitle= { 123 }/> */}
        {/* <FirstApp title="Hola, Soy Cristian" />  */}
        < CounterApp value={1} />
    </React.StrictMode>
);