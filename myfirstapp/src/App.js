//import logo from './logo.svg';
import './App.css';


function Helloworld(props) {
  console.log(props)
  return (
    <div id="hello">{props.mytext}</div>
  );
}

//const App = () => <div> This is my component: <Helloworld/> </div>

/*class App extends React.Component {
  render() {
    return <div>This is my component <Helloworld/></div>
  }
}*/

function App() {
  return (
    <div>
      This is my component: 
      <Helloworld mytext ="Hello Cristian"/> 
      <Helloworld mytext="Hola mundo"/> 
      <Helloworld mytext="Hola!!"/>
    </div>
  );
}

export default App;
