
const skills: string[] = ['Bash','Counter','Healing']; //Si nunca va a cambiar es mejor manejar constantes

interface Character {
    name: string;
    hp: number;
    skills: string[];
    hometown?: string | undefined; //es opcional
}

const strider: Character = {
    name: 'Strider',
    hp: 100,
    skills: ['Bash','Counter'],
}

strider.name = 'Rinvendell';

console.table(strider);



export {} //Transformamos el archivo en un modulo del archivo