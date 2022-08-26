import React from 'react';
import ReactDOM from 'react-dom/client';
import { BrowserRouter, Route, Routes } from "react-router-dom";
import reportWebVitals from './reportWebVitals';



// Componentes
import Navbar from './components/Navbar/Navbar';
import CompanyList from './components/Company/CompanyList';
import CompanyForm from './components/Company/CompanyForm';

import "bootstrap/dist/css/bootstrap.min.css";
import "bootstrap/dist/js/bootstrap.js";

import './index.css';


const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
  <BrowserRouter>
    <Navbar />
    <div className='container my-4'>
      <Routes>
        <Route exact path="/" element={<CompanyList/>} />
        <Route exact path="/companyForm" element={<CompanyForm/>} />
        <Route exact path="/updateCompany/:id" element={<CompanyForm />} />
      </Routes>
    </div>
  </BrowserRouter>
);

// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
reportWebVitals();
