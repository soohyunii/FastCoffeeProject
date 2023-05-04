<template>
  <img alt="Vue logo" src="./assets/coffee_bean.png">
  <HelloWorld msg="커피원두 주문하기"/>
  <OrderList></OrderList>
</template>

<script>
import HelloWorld from './components/HelloWorld.vue'
import OrderList from './components/OrderList.vue'

export default {
  name: 'App',
  components: {
    HelloWorld,
    OrderList
  },
  data() {
    return {
      title:'',
      author:'',
      output:''
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
