import logo from './aiB9uGsQ4wk.png';
import './App.css';


function App() {
  var c = 3;
  return (
    <div className="App">
      <header className="App-header">
        <h1 className="H">{c}</h1>
        <img src={logo} className="App-logo" alt="logo" />
        <body>
          <button className="Button" onClick={() => c -= 0.5}>Фронтенд</button>
        </body>
      </header>
    </div>
    
  );
};

export default App;
