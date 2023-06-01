import logo from './aiB9uGsQ4wk.png';
import './App.css';


const Header = () => {
  return (
    <header src='./logo192.png'>AAAA</header>
  );
}

const App = () => {
  var c = 3;
  return (
    <div className="App">
      <header className="App-header">
        <h1 className="H">{c}</h1>
        <img src={logo} className="App-logo" alt="logo" />
        <body>
          <button className="Button" onClick={() => c -= 0.5}>Вротэнд</button>
        </body>
      </header>
    </div>
    
  );
};

export default App;
export var a = Header;
