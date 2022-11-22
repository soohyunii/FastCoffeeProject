<template>
  <img alt="Vue logo" src="./assets/logo.png">
  <HelloWorld msg="Welcome to Your Vue.js App"/>
  <div id="contents">
    <input type="text" placeholder="title" v-model="title">
    <input type="text" placeholder="author" v-model="author">
    <button type="submit" @click="formSubmit()">submit</button>
    <input type="text" placeholder="output" v-model="output">
  </div>
</template>

<script>
import HelloWorld from './components/HelloWorld.vue'
import axios from 'axios'

export default {
  name: 'App',
  components: {
    HelloWorld
  },
  data() {
    return {
      title:'',
      author:'',
      output:''
    }
  },
  methods: {
    formSubmit () {
      axios.post('/form_receiver', {
        title: this.title,
        author: this.author
      })
      .then((response) => {
        this.output = response.data
        this.title = ''
        this.author = ''
      })
      .catch((error) => {
        this.output = error
      })
    }
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
