# Sistema de Gestión de Fondos

Este proyecto es una aplicación web para gestionar la información de clientes, fondos y transacciones, utilizando Vue.js en el frontend y FastAPI en el backend. Incluye funcionalidades para suscribir y cancelar fondos, así como notificaciones por correo electrónico o SMS, dependiendo de la selección del usuario.

## Arquitectura del Sistema

La arquitectura del sistema se basa en una SPA (Single Page Application) construida con Vue.js para el frontend, interactuando con un backend desarrollado en FastAPI y MongoDB como base de datos. Los contenedores Docker se utilizan para gestionar el entorno de desarrollo y despliegue.

## Componentes Utilizados

- **Frontend**: Vue.js, Axios para la comunicación con la API.
- **Backend**: FastAPI para la creación de la API RESTful.
- **Base de Datos**: MongoDB, utilizando PyMongo para la gestión de datos.
- **Contenedores**: Docker para la creación de entornos de backend y frontend.
- **Notificaciones**: 
  - Email: Utilizando `aiosmtplib` y `email-validator` para el envío de correos electrónicos.
  - SMS: Usando Twilio, con un plan gratuito que permite el envío de mensajes solo a números verificados.

## Requerimientos

Antes de empezar, asegúrate de tener instaladas las siguientes herramientas en tu entorno:

Docker: Instalar Docker
Git: Instalar Git
Python 3.9+: Para FastAPI
Node.js 14+: Para Vue.js
MongoDB: Instalar MongoDB

A continuación se enumeran los pasos para clonar y correr el proyecto en local:

### Clonar el Proyecto

git clone https://github.com/usuario/sistema-fondos.git
cd sistema-fondos


### Correr el contenedor
docker-compose up --build

Esto levantará tanto el backend como el frontend en sus respectivos contenedores.

Acceso a la Aplicación
Una vez que los contenedores estén corriendo, puedes acceder a la aplicación desde tu navegador en la siguiente URL:

Frontend: http://localhost:8080
Backend: http://localhost:8000
