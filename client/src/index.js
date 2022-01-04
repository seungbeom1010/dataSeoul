import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';
import App from './App';
import { BrowserRouter, Routes, Route } from 'react-router-dom';
import ScrollToTopOnRoute from './components/ScrollToTopOnRoute';

ReactDOM.render(
  <React.StrictMode>
    <BrowserRouter>
      <ScrollToTopOnRoute />
      <Routes>
        <Route path="/">
          <Route index element={<App />} />
          <Route path=":cityId" element={<App />} />
        </Route>
      </Routes>
    </BrowserRouter>
  </React.StrictMode>,
  document.getElementById('root')
);
