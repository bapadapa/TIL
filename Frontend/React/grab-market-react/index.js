import React from "react";
import ReactDom from "react-dom";
import App from "./src/App";
import { BrowserRouter } from "react-router-dom";
import "./index.css";

ReactDom.render(
  <React.StrictMode>
    <BrowserRouter>
      <App />
    </BrowserRouter>
  </React.StrictMode>,
  document.getElementById("root")
);
