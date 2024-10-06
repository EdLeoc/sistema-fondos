<template>
  <div>
    <h1>Transacciones y Productos</h1>

    <h2>Transacciones</h2>
    <ul>
      <li v-for="transaction in transactions" :key="transaction.id">
        {{ transaction.product_id }} - {{ transaction.amount }}
        <button @click="subscribe(transaction.product_id)">Suscribir</button>
        <button @click="editClientInfo(transaction.client_id)">Editar Información del Cliente</button>
      </li>
    </ul>

    <h2>Productos</h2>
    <ul>
      <li v-for="product in products" :key="product.id">{{ product.name }}</li>
    </ul>
  </div>
</template>

<script>
import axios from 'axios';
export default {
  data() {
    return {
      transactions: [],
      products: [],
    };
  },
  async created() {
    this.transactions = (await axios.get('http://localhost:8000/transactions')).data;
    this.products = (await axios.get('http://localhost:8000/products')).data;
  },
  methods: {
    subscribe(productId) {
      this.$router.push(`/subscribe?product_id=${productId}`);
    },
    editClientInfo(clientId) {
      this.$router.push(`/edit-client?client_id=${clientId}`);
    },
  },
};
</script>

<style scoped>
/* Estilos específicos para este componente */
h1 {
  color: #333;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  padding: 10px;
  margin: 10px 0;
  background-color: #f9f9f9;
  border-radius: 5px;
}
button {
  margin-left: 10px;
}
</style>
