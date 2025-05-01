<template>
<div class="container">
  <!-- Titulo -->
  <div class="title">
      <h1>Juego del Ahorcado</h1>
  </div>
  <div class="content">
      <Input v-if="!juegoIniciado" @iniciar="iniciarJuego" />
      <JuegoAhorcado 
        v-else 
        :palabra="palabraAdivinar" 
        @reiniciar="reiniciarJuego" />
  </div>
  <div class="footer">
    <p>&copy; 2025 - Cristian Gonzalez Arango</p>
  </div>
</div>
</template>

<script setup>
// importaciones
import { ref } from 'vue'
import Input from './components/Input.vue'
import JuegoAhorcado from './components/JuegoAhorcado.vue'

//Logica del juego 
const palabraAdivinar = ref('');
const juegoIniciado = ref(false);

const iniciarJuego = (palabra) => {
  palabraAdivinar.value = palabra;
  juegoIniciado.value = true;
}

const reiniciarJuego = () => {
  palabraAdivinar.value = '';
  juegoIniciado.value = false;
}

</script>

<style scoped>

.title{
  font-size: 20px;
  font-family: 'Times New Roman', Times, serif;
  text-shadow: #0d0b0b 2px 2px 2px;
}

.container{
  text-align: center;
  margin-top: 20px;
  background: #434242;
  height: auto;
  padding-bottom: 30px;
}

.footer p{
  width: auto;
  font-size: 15px;
  color: #4398d8;
}

</style>
