
export interface Product{
    description: string;
    price: number;
}

const phone: Product = {
    description: "Smartphone Samsung Galaxy S21",
    price: 899.99,
}

const tablet: Product = {
    description: "Tablet Samsung Galaxy Tab A",
    price: 499.99,

}

interface taxCalculationOptions{
    tax: number;
    products: Product[];
}

// function taxCalculation( options: taxCalculationOptions ): [number, number]{
export function taxCalculation( options: taxCalculationOptions ): [number, number]{

    const { tax, products } = options;
    let total = 0;
    products.forEach(( { price }) => {
        total += price;
    });
    
    return [total, total * tax];
}

const shoppingCart = [phone, tablet];
// const tax = 0.15;
const [total, taxTotal] = taxCalculation({
    products: shoppingCart,
    tax: 0.15,
});

console.log('Total', total);
console.log('Tax', taxTotal);


// export {}