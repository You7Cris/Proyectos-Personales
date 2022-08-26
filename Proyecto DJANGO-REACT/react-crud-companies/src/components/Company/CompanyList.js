import React, { useEffect, useState } from "react";

//Componente 
import CompanyItem from "./CompanyItem";

import * as CompanyServer from './CompanyServer';

const CompanyList = () => {
  /*const initialState = [
    {
      id: 1,
      name: "Facebook",
      foundation: 2004,
    },
    {
      id: 2,
      name: "Google",
      foundation: 2008,
    },
  ];*/
  const [companies, setCompanies] = useState([]); //Crea un atributo llamado companies y un metodo llamado setCompanies que va a permitir modificar, useState hace parte del estado y que en el inicio tenga un arreglo vacio.
  const listCompanies = async () => {
    try{
      const res = await CompanyServer.listCompanies();
      const data = await res.json();
      setCompanies(data.companies);
    }catch (error) {
      console.log(error);
    }
  };

  useEffect(() => {
    listCompanies();
  },[]);

  return (
    <div className="row">
      {companies.map((company)=>(
        <CompanyItem key={company.id} company={company} listCompanies={listCompanies} />
      ))} 
    </div>
  ); //map es para recorrer como un ciclo for
};

export default CompanyList;
