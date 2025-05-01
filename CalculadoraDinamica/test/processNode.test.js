const { processNode } = require('../src/processNode');
const { processMultipleNode } = require('../src/processMultipleNode');

describe('Operaciones válidas', () => {
  it('Debe sumar correctamente los números', () => {
    const node = { operation: 'add', params: [1, 2, 3] };
    const resultado = processNode(node);
    expect(resultado.response).toBe(6); // 1 + 2 + 3 = 6
  });

  it('Debe restar correctamente los números', () => {
    const node = { operation: 'subtract', params: [10, 5, 3] };
    const resultado = processNode(node);
    expect(resultado.response).toBe(2); // 10 - 5 - 3 = 2
  });

  it('Debe multiplicar correctamente los números', () => {
    const node = { operation: 'multiply', params: [2, 3, 4] };
    const resultado = processNode(node);
    expect(resultado.response).toBe(24); // 2 * 3 * 4 = 24
  });

  it('Debe dividir correctamente los números (division secuencial)', () => {
    const node = { operation: 'divide', params: [8, 2, 2] };
    const resultado = processNode(node);
    expect(resultado.response).toBe(2); // 8 / 2 / 2 = 2
  });

  it('Debe calcular la raíz cuadrada de un número', () => {
    const node = { operation: 'sqrt', params: [9] };
    const resultado = processNode(node);
    expect(resultado.response).toBe(3); // √9 = 3
  });

  it('Debe calcular la potenciación correctamente', () => {
    const node = { operation: 'power', params: [2, 3] };
    const resultado = processNode(node);
    expect(resultado.response).toBe(8); // 2^3 = 8
  });
});

describe('Operaciones inválidas', () => {
  it('Debe lanzar un error si la operación no es válida', () => {
    const node = { operation: 'suma', params: [2, 3] };
    expect(() => processNode(node)).toThrow('Operación no soportada');
  });

  it('Debe lanzar un error si los parámetros están vacíos en add', () => {
    const node = { operation: 'add', params: [] };
    expect(() => processNode(node)).toThrow('Los parámetros no pueden estar vacíos');
  });

  it('Debe lanzar un error si los parámetros no son números en add', () => {
    const node = { operation: 'add', params: [2, 'a', 3] };
    expect(() => processNode(node)).toThrow('Todos los parámetros deben ser números');
  });
});

describe('Múltiples nodos procesados correctamente', () => {
  it('Debe procesar múltiples nodos correctamente', () => {
    const nodes = [
      { operation: 'add', params: [1, 2] },
      { operation: 'subtract', params: [10, 5] },
      { operation: 'multiply', params: [2, 3] },
      { operation: 'divide', params: [8, 2] }
    ];
    const resultados = processMultipleNode(nodes);
    expect(resultados[0].response).toBe(3); // 1 + 2 = 3
    expect(resultados[1].response).toBe(5); // 10 - 5 = 5
    expect(resultados[2].response).toBe(6); // 2 * 3 = 6
    expect(resultados[3].response).toBe(4); // 8 / 2 = 4
  });
});
