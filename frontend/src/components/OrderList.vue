<template>
    <div id="contents">
        <label>현재 재고</label>
        <input type="text" placeholder="현재 재고" v-model="now_stock"><p></p>
        <label>주문 개수</label>
        <input type="text" placeholder="주문 개수" v-model="order_stock"><p></p>
        <label>주문 매장</label>
        <input type="text" placeholder="주문 매장" v-model="store"><p></p>
        <button type="submit" @click="formSubmit()">제출하기</button>
    </div>
</template>

<script>
import axios from 'axios'

export default ({
    name: 'OrderList',
    props:{

    },
    methods: {
        formSubmit () {
        axios.post('/form_receiver', {
            now_stock: this.now_stock,
            order_stock: this.order_stock,
            store: this.store
        })
        .then((response) => {
            this.store = response.now_stock
            this.title = ''
            this.author = ''
        })
        .catch((error) => {
            this.store = error
        })
        }
    }
})

</script>

<style>
#contents {
    margin-top: 80px;
}
input {
    margin-left: 10px;
}
button {
    margin-top: 30px;
    padding: 10px 20px;
}
</style>