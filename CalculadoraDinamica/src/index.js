const express = require('express');
const { processNode } = require('./processNode');
const { processMultipleNode } = require('./processMultipleNode');

const app = express();

app.use(express.json());

app.get('/', (req, res) => {
  res.send('Calculadora dinamica de operaciones matematicas');
});

app.post('/calcular', (req, res) => {
    try{
        const node = req.body;
        console.log('Datos recibidos en: ', node);
        const resultado = processNode(node);
        res.json(resultado);
    }catch(error){
        res.status(400).json({ error: error.message });
    }
});

app.post('/calcular-multiples', (req, res) => {
    try{
        const nodes = req.body;
        const resultados = processMultipleNode(nodes);
        res.json(resultados);
    }catch(error){
        res.status(400).json({ error: error.message });
    }
});

const PORT = 3000;
app.listen(PORT, () => {
  console.log(`Servidor corriendo en el puerto ${PORT}`);
});