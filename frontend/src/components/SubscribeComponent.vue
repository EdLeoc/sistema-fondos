<template>
  <div>
    <h1>Suscribir a un Fondo</h1>

    <label for="amount">Cantidad a suscribir:</label>
    <input v-model="amount" type="number" />

    <button @click="openModal">Continuar</button>

    <!-- Modal -->
    <div v-if="showModal">
      <h2>Seleccione el modo de notificación</h2>
      <select v-model="notificationMethod">
        <option value="email">Email</option>
        <option value="sms">SMS</option>
      </select>
      <button @click="subscribe">Confirmar</button>
    </div>
  </div>
</template>

<script>
import axios from 'axios';
export default {
  data() {
    return {
      amount: 0,
      notificationMethod: 'email',
      showModal: false,
    };
  },
  methods: {
    openModal() {
      this.showModal = true;
    },
    async subscribe() {
      try {
        await axios.post('http://localhost:8000/transactions', {
          client_id: '1',
          product_id: this.$route.query.product_id,
          amount: this.amount,
          type: 'subscription',
          notification_method: this.notificationMethod,
        });
        alert('Suscripción exitosa');
        this.$router.push('/');
      } catch (error) {
        alert('Error: ' + error.response.data.detail);
      }
    },
  },
};
</script>

<style scoped>
/* Estilos para el componente de suscripción */
input {
  margin: 10px;
  padding: 5px;
}
button {
  margin: 10px;
}
</style>
