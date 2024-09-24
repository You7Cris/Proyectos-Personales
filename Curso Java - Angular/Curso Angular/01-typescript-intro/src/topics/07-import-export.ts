// interface Product {
//     description: string;
//     price: number;
// }

import { Product, taxCalculation } from './06-functions-desestructuring';



const shoppingCart: Product[] = [
    {
        description: 'Nokia',
        price: 100
    },
    {
        description: 'Samsung',
        price: 140
    }
    
];

const [total, tax] = taxCalculation({
    products: shoppingCart,
    tax: 0.15
});

console.log('Total', total);
console.log('Tax', tax);