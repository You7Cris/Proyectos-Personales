<template>
    <div style="margin-top: 20px;">
        <p>
        Palabra:
        <span v-for="(letra, index) in palabra" :key="index" style="letter-spacing: 0.5em; color: #cb7825; font-weight: bold;">
            {{ letrasAdivinadas.includes(letra.toLowerCase()) ? letra : '_' }}
        </span>
        </p>

        <p>Errores: {{ letrasEquivocadas.length }} / 6</p>
        <p>Letras falladas: {{ letrasEquivocadas.join(', ') }}</p>

        <input
        v-model="letras"
        @keydown.enter="adivinarLetra"
        @input="validarLetras"
        maxlength="1"
        :disabled="juegoPerdido"
        />
        <button @click="adivinarLetra" :disabled="juegoPerdido">Adivinar</button>
        <p v-if="estado === 'gano'">🎉 ¡Ganaste!</p>
        <p v-else-if="estado === 'perdio'">💀 Perdiste. La palabra era: {{ palabra }}</p>

        <button @click="emit('reiniciar')">Reiniciar</button>

        <!-- Dibujo -->
        <div class="ahorcado">
            <div class="poste"></div>
            <div class="barra-horizontal"></div>
            <div class="cuerda"></div>
            <div v-if="errores >= 1" class="cabeza"></div>
            <div v-if="errores >= 2" class="torso"></div>
            <div v-if="errores >= 3" class="brazo izquierdo"></div>
            <div v-if="errores >= 4" class="brazo derecho"></div>
            <div v-if="errores >= 5" class="pierna izquierda"></div>
            <div v-if="errores >= 6" class="pierna derecho"></div>
        </div>
    </div>
</template>

<script setup>
import { ref, computed, watch } from 'vue'

const props = defineProps({
  palabra: {
    type: String,
    required: true
  }
})

const emit = defineEmits(['reiniciar']) // cuando se emita el evento reiniciar

const letrasAdivinadas = ref([])
const letrasEquivocadas = ref([])
const letras = ref('')
const errores = computed(() => letrasEquivocadas.value.length) //Para que se dibuje el cuerpo del ahorcado

const palabraNormalizada = computed(() => props.palabra.toLowerCase())

// Se actualiza en tiempo real 
const estado = computed(() => {
  const unicasLetras = [...new Set(palabraNormalizada.value)]
  if (unicasLetras.every(letra => letrasAdivinadas.value.includes(letra))) return 'gano'
  if (letrasEquivocadas.value.length >= 6) return 'perdio'
  return 'jugando'
})

//Se actualiza en tiempo real
const juegoPerdido = computed(() => estado.value !== 'jugando') //Propiedad computada que devuelve un booleano

const validarLetras = () => {
  letras.value = letras.value.replace(/[^a-zA-ZáéíóúÁÉÍÓÚñÑ]/g, '') // elimina caracteres no alfanuméricos
}

const adivinarLetra = () => {
  const letra = letras.value.toLowerCase()
  if (!letra || letrasAdivinadas.value.includes(letra) || letrasEquivocadas.value.includes(letra)) {
    letras.value = ''
    return
  }

  if (palabraNormalizada.value.includes(letra)) {
    letrasAdivinadas.value.push(letra)
  } else {
    letrasEquivocadas.value.push(letra)
  }

  letras.value = ''
}

// watch es una función que se ejecuta cuando se cambia el valor de una variable
watch(() => props.palabra, (palabra) => {
  letrasAdivinadas.value = []
  letrasEquivocadas.value = []
  letras.value = ''
})
</script>

<style scoped>
p{
    font-size: 20px;
}


.ahorcado {
  position: relative;
  width: 200px;
  height: 250px;
  margin: 2rem auto;
  border: 1px solid transparent;
  margin-bottom: 40px;
}

.poste {
  position: absolute;
  left: 40px;
  width: 10px;
  height: 200px;
  background-color: #ffffff;
}

.barra-horizontal {
  position: absolute;
  top: 0;
  left: 40px;
  width: 100px;
  height: 10px;
  background-color: #ffffff;
}

.cuerda {
  position: absolute;
  top: 10px;
  left: 130px;
  width: 2px;
  height: 40px;
  background-color: #8f8d8d;
}

/* Cuerpo del ahorcado */
.cabeza {
  position: absolute;
  top: 50px;
  left: 115px;
  width: 30px;
  height: 30px;
  border-radius: 50%;
  background-color:#f18c8c;
}

.torso {
  position: absolute;
  top: 80px;
  left: 129px;
  width: 2px;
  height: 80px;
  background-color: #f18c8c;
}

.brazo.izquierdo {
  position: absolute;
  top: 100px;
  left: 129px;
  width: 40px;
  height: 2px;
  background-color: #f18c8c;
  transform: rotate(-30deg);
  transform-origin: left;
}

.brazo.derecho {
  position: absolute;
  top: 100px;
  left: 92px;
  width: 40px;
  height: 2px;
  background-color: #f18c8c;
  transform: rotate(30deg);
  transform-origin: right;
}

.pierna.izquierda {
  position: absolute;
  top: 158px;
  left: 129px;
  width: 40px;
  height: 2px;
  background-color: #f18c8c;
  transform: rotate(30deg);
  transform-origin: left;
}

.pierna.derecho {
  position: absolute;
  top: 158px;
  left: 90px;
  width: 40px;
  height: 2px;
  background-color: #f18c8c;
  transform: rotate(-30deg);
  transform-origin: right;
}
</style>