interface AudioPlayer {
    audioVolume: number;
    songDuration: number;
    song: string;
    details: Details;
}

interface Details{
    author: string;
    year: number;
}

const audioPlayer: AudioPlayer = {
    audioVolume: 90,
    songDuration: 36,
    song: "Mess",
    details: {
        author: "Cristian Gonzalez",
        year: 2024
    }
}

const song = 'New Song';
const { 
    song:anotherSong, 
    songDuration:duration,
    details
} = audioPlayer;

const { author } = details;

// console.log('Song', song);
// console.log('Duration', duration);
// console.log('Author: ', author);
// console.log('Song: ', audioPlayer.song);
// console.log('Author: ', audioPlayer.details.author);
// console.log('Duration: ', audioPlayer.songDuration);

const dbz: string[] = ['Goku', 'Vegeta', 'Trunks'];
const trunk = dbz[3] || 'No hay personaje';

console.log('Personaje 3:', trunk);



export {}