<template>
  <div>
    <h2>Editar Información del Cliente</h2>
    <form @submit.prevent="updateClient">
      <div>
        <label for="name">Nombre:</label>
        <input
          id="name"
          v-model="client.name"
          @input="handleInput"
          required
          type="text"
        />
      </div>
      <div>
        <label for="last_name">Apellido:</label>
        <input
          id="last_name"
          v-model="client.last_name"
          @input="handleInput"
          required
          type="text"
        />
      </div>
      <div>
        <label for="city">Ciudad:</label>
        <input
          id="city"
          v-model="client.city"
          @input="handleInput"
          required
          type="text"
        />
      </div>
      <div>
        <label for="email">Correo Electrónico:</label>
        <input
          id="email"
          v-model="client.email"
          @input="handleInput"
          required
          type="email"
        />
      </div>
      <div>
        <label for="balance">Saldo:</label>
        <input
          id="balance"
          v-model="client.balance"
          @input="handleInput"
          required
          type="number"
        />
      </div>

      <!-- Botón de Guardar Cambios -->
      <button :disabled="!isModified" type="submit">Guardar Cambios</button>

      <!-- Botón de Volver -->
      <button @click="goBack">Volver</button>
    </form>
  </div>
</template>

<script>
import axios from 'axios'
export default {
  data() {
    return {
      client: {
        name: "",
        last_name: "",
        city: "",
        email: "",
        balance: 0,
      },
      originalClient: {}, // Para almacenar los datos originales del cliente
      isModified: false,  // Estado para habilitar/deshabilitar el botón de guardar
    };
  },
  async mounted() {
    const response = await axios.get(`http://localhost:8000/clients/1`);
    this.client = response.data;
    this.originalClient = { ...response.data }; // Copiamos los datos originales
  },
  methods: {
    // Detectar cambios en los inputs
    handleInput() {
      this.isModified = this.checkIfModified(); // Verifica si algo cambió
    },
    // Verificar si hay diferencias entre los datos originales y los actuales
    checkIfModified() {
      return (
        this.client.name !== this.originalClient.name ||
        this.client.last_name !== this.originalClient.last_name ||
        this.client.city !== this.originalClient.city ||
        this.client.email !== this.originalClient.email ||
        this.client.balance !== this.originalClient.balance
      );
    },
    // Método para actualizar el cliente
    async updateClient() {
      try {
        const clientId = '1'; // Cambia esto si el client_id es dinámico
        await axios.put(`http://localhost:8000/clients/${clientId}`, this.client);
        alert("Información del cliente actualizada correctamente.");
        this.$router.push("/listados");
      } catch (error) {
        alert("Error al actualizar la información del cliente.");
        console.log(error);
      }
    },
    // Botón para volver a la página anterior
    goBack() {
      this.$router.push("/listados"); // Redirige a la página de listados
    },
  },
};
</script>

