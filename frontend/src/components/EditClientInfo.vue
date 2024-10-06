<template>
  <div>
    <h1>Editar Información del Cliente</h1>
    <label>Nombre:</label>
    <input v-model="client.name" />
    <label>Apellido:</label>
    <input v-model="client.last_name" />
    <label>Ciudad:</label>
    <input v-model="client.city" />
    <label>Email:</label>
    <input v-model="client.email" />

    <button :disabled="!formChanged" @click="saveChanges">Guardar Cambios</button>
    <button @click="goBack">Volver</button>
  </div>
</template>

<script>
import axios from 'axios';
export default {
  data() {
    return {
      client: {},
      initialClientData: {},
    };
  },
  async created() {
    const clientId = this.$route.query.client_id;
    const response = await axios.get(`http://localhost:8000/clients/${clientId}`);
    this.client = response.data;
    this.initialClientData = { ...this.client }; // Guardar los datos iniciales
  },
  computed: {
    formChanged() {
      return JSON.stringify(this.client) !== JSON.stringify(this.initialClientData);
    },
  },
  methods: {
    async saveChanges() {
      const clientId = this.$route.query.client_id;
      await axios.put(`http://localhost:8000/clients/${clientId}`, this.client);
      alert('Información actualizada con éxito');
      this.goBack();
    },
    goBack() {
      this.$router.push('/');
    },
  },
};
</script>
