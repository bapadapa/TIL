import React from "react";
import ReactDOM from "react-dom";
import "./index.css";
import App from "./App";
import reportWebVitals from "./reportWebVitals";
import ParentComponent from "./Parent";
import SayHelloComponent3 from "./sayHello";
import TimeComponent from "./Time";
//import Component from "./Component";
import ComponentOnlyOnce from "./ComponentOnlyOnce";
ReactDOM.render(
  <React.StrictMode>
    <App />
    <ParentComponent name="Bapa" />
    <SayHelloComponent3 />
    <TimeComponent />
    <ComponentOnlyOnce />
  </React.StrictMode>,
  document.getElementById("root")
  //위아래 동일한 기능을 한다!
  //document.querySelector("#root")
);

// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
reportWebVitals();
