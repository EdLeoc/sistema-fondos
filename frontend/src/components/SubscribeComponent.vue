<template>
  <div>
    <h1>Suscribirse a un Fondo</h1>
    <form @submit.prevent="showNotificationModal">
      <input v-model="fundId" placeholder="ID del Fondo" />
      <input v-model="amount" placeholder="Cantidad" />
      <button type="submit">Suscribirse</button>
    </form>
    <button @click="goBack">Volver</button>

    <!-- Modal de selección de notificación -->
    <div v-if="showModal" class="modal">
      <div class="modal-content">
        <h2>Selecciona cómo deseas recibir la notificación</h2>
        <label for="notificationMethod">Método de notificación:</label>
        <select v-model="notificationMethod">
          <option value="email">Email</option>
          <option value="sms">SMS</option>
        </select>
        <button @click="confirmSubscription">Confirmar</button>
        <button @click="cancelModal">Cancelar</button>
      </div>
    </div>

    <hr>
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
  data() {
    return {
      fundId: '',
      amount: '',
      minAmount: 0,
      userBalance: 0,
      notificationMethod: 'email',  // Valor predeterminado
      showModal: false,
      products: []
    }
  },
  async created() {
    try {
      const userResponse = await axios.get('http://localhost:8000/clients/1')
      this.userBalance = userResponse.data.balance
      this.fetchProducts();
    } catch (error) {
      alert('Error al obtener el saldo del usuario: ' + error.response.data.detail)
    }
  },
  methods: {
    goBack() {
      this.$router.push("/listados"); // Redirige a la página de listados
    },
    async fetchProducts() {
      const response = await axios.get('http://localhost:8000/products');
      this.products = response.data;
    },
    showNotificationModal() {
      // Mostrar el modal de selección de notificación
      this.showModal = true;
    },
    async confirmSubscription() {
      try {
        // Obtener detalles del fondo para verificar el monto mínimo
        const productResponse = await axios.get(`http://localhost:8000/products/${this.fundId}`)
        this.minAmount = productResponse.data.min_amount

        // Validar el monto de suscripción
        if (this.amount < this.minAmount) {
          alert(`La cantidad debe ser mayor o igual al monto mínimo de ${this.minAmount}`)
          this.showModal = false
          return
        }

        // Validar el saldo del usuario
        if (this.amount > this.userBalance) {
          alert(`No tiene suficiente saldo disponible. Su saldo es ${this.userBalance}`)
          this.showModal = false
          return
        }

        // Realizar la suscripción con la opción de notificación
        await axios.post('http://localhost:8000/transactions', {
          client_id: '1',  // Asumimos un ID de usuario de prueba
          product_id: this.fundId,
          amount: this.amount,
          type: 'subscription',
          notification_method: this.notificationMethod  // Opción para notificación
        })

        // Si la suscripción es exitosa, actualizar el saldo del usuario
        this.userBalance -= this.amount
        alert('Suscripción realizada con éxito')
        this.showModal = false
        this.$router.push('/listados');

      } catch (error) {
        alert('Error al realizar la suscripción: ' + error.response.data.detail)
        this.showModal = false
      }
    },
    cancelModal() {
      // Cerrar el modal si se cancela
      this.showModal = false;
    }
  }
}
</script>

<style>
/* Estilos para el modal */
.modal {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-color: rgba(0, 0, 0, 0.5);
  display: flex;
  justify-content: center;
  align-items: center;
}

.modal-content {
  background-color: white;
  padding: 20px;
  border-radius: 10px;
  text-align: center;
}

button {
  margin-top: 10px;
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
</style>
