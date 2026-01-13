#!/bin/sh
set -e

host="$MYSQL_HOST"
user="$MYSQL_USER"
password="$MYSQL_PASSWORD"
db="$MYSQL_DATABASE"

export MYSQL_PWD="$password"
export MYSQL_SSL_MODE=DISABLED

echo "⏳ Waiting for MySQL at $host..."

# Primero esperamos a que MySQL esté listo usando root
until mysqladmin ping -h"$host" -uroot -p"$MYSQL_ROOT_PASSWORD" --skip-ssl --silent 2>/dev/null; do
  echo "   MySQL not ready yet..."
  sleep 2
done

echo "⏳ Checking database '$db' and user access..."
# Verificar que el usuario puede acceder a la base de datos
until mysql -h"$host" -u"$user" -p"$password" --skip-ssl -e "USE $db;" >/dev/null 2>&1; do
  echo "   Database or user not ready yet..."
  sleep 2
done

echo "✅ MySQL is ready with user '$user' — starting FastAPI"
exec "$@"
