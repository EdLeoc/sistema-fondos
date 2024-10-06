<template>
  <div class="list-page">
    <!-- Información del Cliente -->
    <div v-if="client">
      <h2>Información del Cliente</h2>
      <p>Nombre: {{ client.name }} {{ client.last_name }}</p>
      <p>Email: {{ client.email }}</p>
      <p>Ciudad: {{ client.city }}</p>
      <p>Balance: {{ client.balance }}</p>
    </div>
    <button @click="navigateToEditClient">Editar Información del Cliente</button>
    <button @click="goBack">Volver al inicio</button>
    <br>
    <p>Nota: Puede cambiar el correo para comprobar el servicio de notificación por email.</p>
    <hr>
    <h1>Transacciones</h1>
    <table>
      <thead>
        <tr>
          <th>ID Transacción</th>
          <th>ID Cliente</th>
          <th>ID Producto</th>
          <th>Cantidad</th>
          <th>Tipo</th>
          <th>Acciones</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="transaction in transactions" :key="transaction.id">
          <td>{{ transaction.id }}</td>
          <td>{{ transaction.client_id }}</td>
          <td>{{ transaction.product_id }}</td>
          <td>{{ transaction.amount }}</td>
          <td>
            <p v-if="transaction.type === 'subscription'">Suscripción</p>
            <p v-else>Cancelación</p>
          </td>
          <td>
            <button v-if="transaction.type === 'subscription'" @click="cancelSubscription(transaction.id)">
              Cancelar
            </button>
          </td>
        </tr>
      </tbody>
    </table>

    <button @click="navigateToSubscribe">Suscribir nueva apertura</button>

    <h1>Fondos Registrados</h1>
    <table>
      <thead>
        <tr>
          <th>ID Fondo</th>
          <th>Nombre</th>
          <th>Monto Mínimo</th>
          <th>Categoría</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="product in products" :key="product.id">
          <td>{{ product.id }}</td>
          <td>{{ product.name }}</td>
          <td>{{ product.min_amount }}</td>
          <td>{{ product.category }}</td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'TransactionsProductsList',
  data() {
    return {
      client: null,
      transactions: [],
      products: []
    }
  },
  created() {
    this.fetchTransactions();
    this.fetchProducts();
  },
  methods: {
    goBack() {
      this.$router.push("/");
    },
    navigateToEditClient() {
      this.$router.push(`/edit-client`);
    },
    async fetchTransactions() {
      const response = await axios.get('http://localhost:8000/transactions');
      this.transactions = response.data;
    },
    async fetchProducts() {
      const response = await axios.get('http://localhost:8000/products');
      this.products = response.data;

      const responseClient = await axios.get('http://localhost:8000/clients/1');
      this.client = responseClient.data;
    },
    navigateToSubscribe() {
      this.$router.push('/suscribir');
    },
    async cancelSubscription(transactionId) {
      try {
        const response = await axios.post('http://localhost:8000/transactions/cancel', {
          transaction_id: transactionId
        });
        alert(response.data.message);
        // Recargar las transacciones después de cancelar
        this.fetchTransactions();
        this.fetchProducts()

      } catch (error) {
        console.error('Error al cancelar la transacción:', error);
      }
    }
  }
}
</script>

<style scoped>
.list-page {
  max-width: 800px;
  margin: auto;
}

table {
  width: 100%;
  margin-bottom: 20px;
  border-collapse: collapse;
}

th, td {
  padding: 10px;
  border: 1px solid #ccc;
  text-align: left;
}

button {
  padding: 10px;
  margin-top: 20px;
  font-size: 14px;
}
</style>

