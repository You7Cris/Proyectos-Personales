require('dotenv').config()
const axios = require('axios')


const { createBot, createProvider, createFlow, addKeyword } = require('@bot-whatsapp/bot')

const QRPortalWeb = require('@bot-whatsapp/portal')
const BaileysProvider = require('@bot-whatsapp/provider/baileys')
const MockAdapter = require('@bot-whatsapp/database/mock')


/**
 * Retornar Array con los mensajes
*/
const menuAPI = async () =>{

    const options = {
        method: 'GET',
        //url: 'https://footapi7.p.rapidapi.com/api/search/champions',
        //url: 'https://footapi7.p.rapidapi.com/api/match/10200674',
        url: 'http://api.football-data.org/v4/matches',
        headers: {
            'X-Auth-Token': '7ea9c80b36364478940b361b2dcaa23f',
            'X-Unfold-Goals': true
        //   'X-RapidAPI-Key': '9529a9893amsh0d744c01c0f88e6p1bf1e7jsn943e0f2eb2fb',
        //   'X-RapidAPI-Host': 'footapi7.p.rapidapi.com'
        }
    };

    try {
    const response = await axios.request(options);
    return response.data["matches"].map(results => ({results:[`*Area:* ${area_formato(results.area.name)} ` + '\n' + `*Competencia:* ${results.competition.name}` + '\n' + 
    //Fecha del partido
    `${((results.status) == 'FINISHED') ? '' : formato_fecha(results.utcDate) + '\n'}` +
    //Cambio de estado a español
    `*Estado:* ${estatus(results.status)}`
    + '\n' + 
    //Datos para mostrar el partido con su estado
    // ` ${results.homeTeam.shortName} - ${results.awayTeam.shortName}` + 
    `${mostrar_datos(results.status,
        results.homeTeam.shortName,
        results.awayTeam.shortName,
        results.score.winner,
        results.score.fullTime.home,
        results.score.fullTime.away,
        results.score.halfTime.home,
        results.score.halfTime.away
        )}`
        + '\n'].join('\n')}))
    //return data.map(results => ({results:[`* Equipo: ${results.entity.name}`].join('\n')}))



    } catch (error) {
        console.error(error);
    }

    
}

// Area
function area_formato(area)
{
    if(area == 'South America')
    {
        return 'Sur America'
    }
    if(area == 'Netherlands')
    {
        return 'Holanda'
    }
    if(area == 'Germany')
    {
        return 'Alemania'
    }
    if(area == 'Italy')
    {
        return 'Italia'
    }
    if(area == 'France')
    {
        return 'Francia'
    }
    if(area == 'England')
    {
        return 'Inglaterra'
    }
    if(area == 'Spain')
    {
        return 'España'
    }
    if(area == 'Portugal')
    {
        return 'Portugal'
    }
    else{
        return area
    }
}

//mostrar imagen Ej
function mostrar_imagen(imagen)
{
     
}

function formato_fecha(fecha){
    var date = new Date(fecha);
    var year = date.getFullYear(); // Dia getUTCDate()
    var mes = date.getMonth();
    var dia = date.getUTCDate();
    // if(mes == 1)
    // {
    //     mes = 'Enero';
    // }
    // if (mes == 2)
    // {
    //     mes = 'Febrero';
    // }
    // if (mes == 3)
    // {
    //     mes = 'Marzo';
    // }
    // if(mes == 4)
    // {
    //     mes = 'Abril';
    // }
    // if(mes == 5)
    // {
    //     mes = 'Mayo';
    // }
    // if(mes == 6)
    // {
    //     mes = 'Junio';
    // }
    // if(mes == 7)
    // {
    //     mes = 'Julio';
    // }
    // if(mes == 8)
    // {
    //     mes = 'Agosto';
    // }
    // if(mes == 9)
    // {
    //     mes = 'Septiembre';
    // }
    // if(mes == 10)
    // {
    //     mes = 'Octubre';
    // }
    // if(mes == 11)
    // {
    //     mes = 'Noviembre';
    // }
    // if(mes == 12)
    // {
    //     mes = 'Diciembre';
    // }
    //var fecha_partido = dia + '/' + mes + '/' + year
    var hours = date.getHours();
    var minutes = date.getMinutes();
    var am_pm = hours >= 12 ? 'pm' : 'am';
    hours = hours % 12;
    hours = hours ? hours : 12;
    minutes = minutes < 10 ? '0' + minutes : minutes;
    // Organizar fecha
    dia = (dia < 9 ) ? '0'+ dia : dia;
    mes = mes + 1; //Organizar porque empieza en 0
    mes = ((mes+1) < 9) ? '0' + mes : mes;
    var fecha_formato = dia + '/' + mes + '/' + year ;  
    var strTime = `*Fecha:* ` + fecha_formato + '\t' + ' ' + hours + ':' + minutes + ' ' + am_pm;
    return strTime
}

function mostrar_datos(estado, nombre_local, nombre_visitante, ganador, marcador_local, marcador_visitante, marcador_mediotiempo_local, marcador_mediotiempo_visitante){

    // Validacion de estado para mostrar detalle
    if (estado == 'FINISHED' )
    { 
        // validacion del ganador
        if(ganador == 'HOME_TEAM')
        {
            ganador = nombre_local
        }else{
            ganador = nombre_visitante
        }

        return `*Ganador:* ${ganador}` + '\n' + `${nombre_local} ${marcador_local} - ${marcador_visitante} ${nombre_visitante}`
    }
    if (estado == 'IN_PLAY')
    {
        return nombre_local + ' ' + marcador_local + ' - ' + marcador_visitante + ' ' + nombre_visitante
    }

    if (estado == 'PAUSED')
    {
        return nombre_local + ' ' + marcador_mediotiempo_local + ' - ' + marcador_mediotiempo_visitante + ' ' + nombre_visitante
    }
    else{
        return nombre_local + ' - ' + nombre_visitante
    }


}

function estatus(estatus){
    if (estatus == 'FINISHED')
    {
        return 'Finalizado'
    }
    if(estatus == 'DRAW')
    {
        return 'Empatado'
    }
    if(estatus == 'IN_PLAY')
    {
        return 'En juego'
    }
    if(estatus == 'TIMED')
    {
        return 'En espera de comenzar'
    }
    if(estatus == 'PAUSED')
    {
        return 'Pausado'
    }
}


const flujoPrincipal = addKeyword(['hola','buenas', 'oe', 'Dime los partidos', 'dime'])
.addAnswer(['Bienvenido a un ChatBot de Deportes','Hoy estamos animados!!, este bot te puede mostrar los partidos de las siguientes competiciones.'])
.addAnswer('1. Liga de Brasil.\n2. Premier League\n3. Championship (England)\n4. European Championship\n5. UEFA Champions League\n6. Ligue 1\n7. Bundesliga\n8. Serie A\n9. Eredivise\n10. Primeira League (Portugal)\n11. Copa Libertadores\n12. La Liga\n13. FIFA World Cup')
.addAnswer('Los partidos del dia son los siguientes: ', null, async (ctx,{flowDynamic}) => {

    /* Respuestas dinamicas */
    const data = await menuAPI()
    console.log(data)
    const mapeoLista = data.map((item) => item.results).join('\n')
    await flowDynamic(mapeoLista)
    //const messages = data.map((c) => ({results: c}))
    //await flowDynamic(messages)
    //await flowDynamic(data)




    // setTimeout(() => {
    //     flowDynamic([{body: 'Chelsea vs Liverpool'},{body: 'Barcelona vs Real Madrid'}])
    // },500)
    
})
.addAnswer('Eso son los partidos...')
// .addAnswer('¿Cual es tu email?',{capture:true},(ctx, {fallBack} ) => {
//     if(ctx.body.include('@'))
//     {
//         return fallBack()
//     }
//     console.log('Mensaje entrante: ',ctx.body)
// }) 
//Ya lo toma como si fuera mayuscula o minuscula
// const flujoPrincipal = addKeyword(['hola','buenas'],{
//     sensitive:true
// }).addAnswer('Bienvenido a un ChatBot de chistes')

// Sensible a las mayusculas y minusculas
const flujoSecundario = addKeyword(['Gracias']).addAnswer('Es con mucho gusto')

const main = async () => {
    const adapterDB = new MockAdapter()
    //const adapterFlow = createFlow([flowPrincipal])
    const adapterFlow = createFlow([flujoPrincipal])
    const adapterProvider = createProvider(BaileysProvider)

    createBot({
        flow: adapterFlow,
        provider: adapterProvider,
        database: adapterDB,
    })

    QRPortalWeb()
}

main()
