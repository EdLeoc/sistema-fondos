<template>
  <div class="main-page">
    <h1>Descripción Técnica del Proyecto</h1>
    <p>
      Este proyecto es una aplicación web diseñada para gestionar información de clientes, productos (fondos) y transacciones, implementada utilizando tecnologías modernas como Vue.js para el frontend y FastAPI para el backend. El propósito de la aplicación es permitir que los usuarios puedan suscribirse a productos financieros y gestionar dichas suscripciones de manera eficiente, aprovechando la arquitectura de microservicios y contenedores.
    </p>

    <h2>Arquitectura del Sistema</h2>
    <p>
      La arquitectura del sistema sigue un modelo SPA (Single Page Application) con Vue.js en el frontend, interactuando con una API RESTful desarrollada en FastAPI, alojada en un entorno de contenedores Docker. El uso de contenedores garantiza que el entorno de desarrollo y producción sea consistente, proporcionando una fácil escalabilidad y portabilidad. La base de datos utilizada es MongoDB, una solución NoSQL que permite almacenar la información de manera flexible y escalable.
    </p>

    <h2>Componentes Utilizados</h2>
    <ul>
      <li>
        <strong>Frontend:</strong> Vue.js fue elegido por su simplicidad, reactividad y capacidad de gestionar componentes de manera eficiente en una SPA. La comunicación con el backend se realizó utilizando Axios, lo que facilitó las peticiones HTTP asíncronas y permitió un manejo sencillo de las respuestas.
      </li>
      <li>
        <strong>Backend:</strong> FastAPI se eligió por su rendimiento y facilidad de uso. Es una de las tecnologías más rápidas para crear APIs RESTful en Python, con soporte nativo para la validación de datos y documentación automática con Swagger y OpenAPI. Esto facilita el desarrollo, pruebas y escalabilidad del sistema. Además, FastAPI proporciona la capacidad de manejar peticiones asíncronas de manera eficiente, lo que mejora el rendimiento general del sistema.
      </li>
      <li>
        <strong>Base de Datos:</strong> Se usó MongoDB, una base de datos NoSQL orientada a documentos que ofrece flexibilidad y escalabilidad. MongoDB permite almacenar datos no estructurados, lo que es perfecto para manejar diferentes tipos de transacciones sin necesidad de esquemas rígidos. Además, la integración con PyMongo facilita la interacción con la base de datos desde FastAPI.
      </li>
      <li>
        <strong>Contenedores:</strong> Docker fue utilizado tanto para el frontend como para el backend, asegurando que todas las dependencias necesarias estuvieran correctamente instaladas y configuradas en entornos consistentes. Docker permite una fácil administración del entorno, especialmente en producción, asegurando que el sistema pueda escalar sin problemas.
      </li>
      <li>
        <strong>Notificaciones por Correo Electrónico:</strong> Se implementó un servicio de notificación por correo electrónico utilizando la librería `aiosmtplib` para enviar correos electrónicos de forma asíncrona. La integración con SMTP de Gmail permitió enviar correos electrónicos automáticamente cuando los usuarios se suscriben a un nuevo fondo.
      </li>
      <li>
        <strong>Notificaciones por SMS:</strong> Para las notificaciones por SMS se utilizó el servicio de Twilio, lo que permitió enviar mensajes SMS al teléfono del usuario una vez completada la suscripción. Cabe destacar que este servicio está actualmente limitado al envío de mensajes a mi número de teléfono, ya que la cuenta de Twilio en uso requiere una actualización para habilitar el envío de SMS a otros números.
      </li>
    </ul>

    <h2>Elección de Tecnologías</h2>
    <ul>
      <li>
        <strong>Por qué FastAPI:</strong> FastAPI fue seleccionado por varias razones, principalmente por su velocidad y eficiencia. Comparado con otros frameworks de Python, FastAPI permite manejar más peticiones por segundo, lo cual es esencial para aplicaciones que requieren escalabilidad y tiempos de respuesta bajos. Además, su integración con Pydantic proporciona una excelente validación de datos, lo que reduce la posibilidad de errores.
      </li>
      <li>
        <strong>Por qué Vue.js:</strong> Vue.js fue elegido para el frontend por su curva de aprendizaje suave, flexibilidad y capacidad de crear interfaces interactivas de manera eficiente. Vue permite una fácil gestión del estado y la reutilización de componentes, lo cual es clave para una aplicación SPA donde la interacción del usuario debe ser rápida y sin interrupciones. Además, la comunidad de Vue.js es muy activa, lo que facilita el soporte y la integración de herramientas adicionales.
      </li>
      <li>
        <strong>Por qué MongoDB:</strong> MongoDB fue elegido por su flexibilidad en la gestión de datos, permitiendo almacenar documentos JSON de manera no estructurada. Esto es útil cuando se requiere un modelo de datos que pueda evolucionar con el tiempo sin restricciones de esquema. Además, MongoDB es altamente escalable, lo que lo convierte en una solución ideal para aplicaciones con grandes volúmenes de datos.
      </li>
    </ul>

    <h2>Gestión de Notificaciones</h2>
    <p>
      El proyecto incluye dos tipos de notificaciones: por correo electrónico y por SMS. Los usuarios pueden elegir entre estas opciones al suscribirse a un fondo. Para el envío de correos electrónicos, se utilizó la librería `aiosmtplib`, que permite enviar correos electrónicos de forma asíncrona utilizando servidores SMTP como Gmail. Para las notificaciones por SMS, se utilizó la plataforma Twilio, que permite el envío de mensajes de texto a través de una API sencilla. Aunque el servicio de SMS está actualmente limitado a mi número de teléfono, se puede escalar mediante la habilitación de Twilio para enviar a otros números.
    </p>

    <h2>Pruebas y Calidad del Código</h2>
    <p>
      Durante el desarrollo de la aplicación se consideraron las mejores prácticas para garantizar la calidad del código y la mantenibilidad del proyecto. Se aplicaron principios de Clean Code, asegurando que el código fuera legible, modular y fácil de mantener. Además, se implementaron pruebas unitarias en el backend para garantizar la fiabilidad de los servicios. El manejo de excepciones fue un aspecto clave para garantizar que la aplicación pudiera manejar errores de forma adecuada, proporcionando feedback claro al usuario.
    </p>

    <h2>Conclusión</h2>
    <p>
      Este proyecto demuestra la capacidad de integrar tecnologías modernas como FastAPI, Vue.js y MongoDB para crear una aplicación web eficiente y escalable. La arquitectura basada en microservicios y contenedores garantiza que el sistema sea flexible, fácilmente mantenible y escalable. La integración de servicios como Twilio para SMS y Gmail para correos electrónicos proporciona una funcionalidad completa, asegurando que los usuarios estén siempre informados sobre sus suscripciones. La combinación de estas tecnologías asegura una experiencia de usuario robusta y una base sólida para futuras expansiones.
    </p>

    <button @click="navigateToTransactions">Ver Transacciones y Productos</button>
  </div>
</template>

<script>
export default {
  methods: {
    navigateToTransactions() {
      this.$router.push('/listados');
    }
  }
}
</script>

<style scoped>
.main-page {
  padding: 20px;
  background-color: #f9f9f9;
}

h1 {
  color: #333;
  font-size: 2em;
}

h2 {
  color: #555;
  margin-top: 20px;
  font-size: 1.5em;
}

p {
  color: #666;
  line-height: 1.6;
  margin-bottom: 20px;
}

ul {
  list-style-type: disc;
  margin-left: 20px;
  color: #666;
}

li {
  margin-bottom: 10px;
}

button {
  background-color: #007bff;
  color: white;
  border: none;
  padding: 10px 20px;
  cursor: pointer;
  font-size: 1em;
}

button:hover {
  background-color: #0056b3;
}
</style>
