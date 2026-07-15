#!/usr/bin/env bash

# clase final - 20 script de build para Render
# Detiene el script ante cualquier error.
set -o errexit

# clase final - 20 actualiza pip por compatibilidad de dependencias
python -m pip install --upgrade pip

# clase final - 20 instala dependencias del proyecto
pip install -r requirements.txt

# clase final - 20 recopila archivos estaticos para produccion
python manage.py collectstatic --noinput

# clase final - 20 aplica migraciones de base de datos
python manage.py migrate --noinput

# Crear superusuario por defecto si no existe
python manage.py shell << 'EOF'
from django.contrib.auth import get_user_model

User = get_user_model()
username = "admin"
password = "1234"
email = "admin@gmail.com"

if not User.objects.filter(username=username).exists():
	User.objects.create_superuser(username=username, email=email, password=password)
	print("Superusuario 'admin' creado.")
else:
	print("Superusuario 'admin' ya existe.")
EOF