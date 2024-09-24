export interface Passenger {
    name: string;
    children?: string[];
}

const passenger1: Passenger = {
    name: 'Fernando',
}

const passenger2: Passenger = {
    name: 'Melissa',
    children: ['Jose','Natalia'],
}

const returnChildrenNumber = ( passenger: Passenger) => {


    // const howManyChildren = passenger.children?.length
    // const howManyChildren = passenger.children!.length || 0; 
    const howManyChildren = passenger.children?.length || 0; 

    console.log(howManyChildren);

    return howManyChildren;
}

returnChildrenNumber(passenger1); // Output: 0