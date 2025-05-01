<template>
 
    <div class="input">
        <div style="margin-bottom: 20px">
            <span style="font-size:16px;">Ingrese la palabra para comenzar con el juego.</span>
        </div>
        <input v-model="input" @input="validarInput" placeholder="Ingresa palabra secreta" style="margin-right: 10px;" />
        <button :disabled="!input" @click="comenzar">Iniciar Juego</button>
    </div>
</template>

<script setup>
import { ref } from 'vue'

const emit = defineEmits(['iniciar'])

const input = ref('')

const validarInput = () => {
    input.value = input.value.replace(/[^a-zA-ZáéíóúÁÉÍÓÚñÑ]/g, '')

    if(input.value.length > 12){
        input.value = input.value.slice(0, 12)
    }

}

const comenzar = () => {

    if(input.value.length < 3){
        alert('Ingrese una palabra de al menos 3 letras')
        return
    }

    emit('iniciar', input.value.trim())
    input.value = ''
}

</script>

<style scoped>
.input{
    margin: 20px;
}
</style>