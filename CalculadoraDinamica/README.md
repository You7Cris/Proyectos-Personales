# Calculadora Dinámica

Esta es una calculadora dinamica que permite realizar diferentes operaciones.

Este proyecto fue construido utilizando Node.js, Express y Jest.

## Instalación

* Clonar el repositorio en tu máquina local
* Abrir una terminal en la carpeta del proyecto
* Ejecutar `npm install` para instalar las dependencias
* Ejecutar `npm start` para iniciar el servidor

## Uso

Puedes utilizar cualquier herramienta de tu preferencia para enviar peticiones HTTP a la API, Thunder Client, Postman, etc.

La estructura base es la siguiente:

```json
{
  "operation": "operación",
  "params": [...]
}

La ruta es `/calcular` y el método HTTP es `POST`, cuando solo vas a enviar una operacion.
http://localhost:3000/calcular


```json
{
  "operation": "add",
  "params": [1, 2, 3]
}
```
Si vas a enviar múltiples operaciones, utiliza la ruta `/calcular-multiples` y el método HTTP es `POST`.
http://localhost:3000/calcular-multiples

```json
[
  {
    "operation": "add",
    "params": [1, 2, 3]
  },
  {
    "operation": "subtract",
    "params": [10, 5, 3]
  },
  {
    "operation": "multiply",
    "params": [2, 3, 4]
  },
  {
    "operation": "divide",
    "params": [8, 2, 2]
  }
]

Donde `operation` es la operación a realizar y `params` son los parámetros de la operación.

## Ejemplos

### Suma

```json
{
  "operation": "add",
  "params": [1, 2, 3]
}
```

### Resta

```json
{
  "operation": "subtract",
  "params": [10, 5, 3]
}
```

### Multiplicación

```json
{
  "operation": "multiply",
  "params": [2, 3, 4]
}
```

### División

```json
{
  "operation": "divide",
  "params": [8, 2, 2]
}
```

### Raíz cuadrada

```json
{
  "operation": "sqrt",
  "params": [9]
}
```

### Potenciación

```json
{
  "operation": "power",
  "params": [2, 3]
}
```

## Tests

Para ejecutar los tests, ejecutar `npm test`.

