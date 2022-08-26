const API_URL = "http://127.0.0.1:8000/api/companies/";

export const listCompanies = async () => {
    /*return await fetch('{API_URL}',
    {
        'mode': 'no-cors',
        'headers' : {
            'Acess-Control-Allow-Origin': '*',
        },
        }); //await es para esperar*/
    return await fetch(API_URL);
};