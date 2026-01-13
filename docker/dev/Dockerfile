FROM python:3.12-slim

WORKDIR /app

# Copiar dependencias y archivo de requerimientos
COPY requirements.txt .

# Instalar dependencias del sistema necesarias para mysqladmin y PyMySQL
RUN apt-get update && \
    apt-get install -y default-mysql-client && \
    pip install --no-cache-dir -r requirements.txt && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

# Copiar el resto del proyecto
COPY . .

# Dar permisos de ejecución al script
RUN chmod +x /app/docker/dev/wait-for-db.sh

# Exponer puerto por claridad
EXPOSE 8000

# Comando por defecto
CMD ["/bin/sh", "docker/dev/wait-for-db.sh", "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
