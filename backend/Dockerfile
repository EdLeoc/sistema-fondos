# Imagen base de Python
FROM python:3.9-slim

# Directorio de trabajo
WORKDIR /app

# Archivo de dependencias
COPY ./requirements.txt /app/requirements.txt

# Instalar las dependencias
RUN pip install --no-cache-dir --upgrade pip && pip install -r /app/requirements.txt

# Copiar el resto del código de la aplicación
COPY . /app

# Exponer el puerto 8000 para la API
EXPOSE 8000

# Comando para ejecutar FastAPI
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]

