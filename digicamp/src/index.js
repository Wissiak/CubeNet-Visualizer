import React, { useState } from "react";
import ReactDOM from "react-dom/client";
import "./index.css";
import App from "./App";
import reportWebVitals from "./reportWebVitals";
import Navigation from "./Navigation";

function Main() {
  const [skipReverseAnim, setSkipReverseAnim] = useState(false);
  const [enableHighlight, setEnableHighlight] = useState(true);
  const [net, setNet] = useState(1);

  const config = {
    skipReverseAnim: skipReverseAnim,
    setSkipReverseAnim: setSkipReverseAnim,
    enableHighlight: enableHighlight,
    setEnableHighlight: setEnableHighlight,
    net: net,
    setNet: setNet
  };
  return (
    <>
      <Navigation config={config}/>
      <div className="container">
        <App config={config}/>
      </div>
    </>
  )
}

const root = ReactDOM.createRoot(document.getElementById("root"));
root.render(
  <React.StrictMode>
    <Main />
  </React.StrictMode>
);

// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
reportWebVitals();
