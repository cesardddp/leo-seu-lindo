<script setup lang="ts">
import { onMounted, ref, reactive } from 'vue'
import { parse } from 'node-html-parser';
import axios from 'axios'

let htmlPuro:string = ref('<section><ul id="list"><li>Hello World</li></ul></section>')
// const estrPrimFilho = root.firstChild.structure;
// const querySelector:any = root.querySelector('#list');
// const text = querySelector.firstChild.text


let parseado:object = reactive({html:"default"})

const parsee = ()=>{
  console.log(htmlPuro.value)
  const root = parse(htmlPuro.value)
  // let gasolina = 
  parseado.html = root.querySelector('.gasolina').toString()
  // debugger
  alert("carregou")
}

onMounted(
  ()=>{
    axios.get("http://localhost:5000/")
    .then((response) => {
      // debugger
      htmlPuro.value = response.data
      
      parsee()


    })});

  



</script>

<template>
<span>

<!-- <b>puro: </b>
<p> {{htmlPuro}}</p> -->
<b>Parseado:</b>
<p v-html="parseado.html"></p>
<!-- {{parseado}} -->
</span>
</template>

<style scoped>
span{
  min-width: 80%;
  max-width: 85%;
  border:3px dotted;
  padding: 5rem;
  position: absolute;
  left:0;
}
p{
  margin:2em;
  padding: 1em;
  border:1px solid red;
}
</style>
