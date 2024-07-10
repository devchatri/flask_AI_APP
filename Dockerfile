# Utiliser une image de base officielle de Python
FROM python:3.9-slim

# Définir le répertoire de travail dans le conteneur
WORKDIR /app

# Copier le fichier requirements.txt dans le répertoire de travail
COPY requirements.txt .

# Installer les dépendances Python
RUN pip install --no-cache-dir -r requirements.txt

# Copier tout le contenu de votre projet dans le répertoire de travail
COPY . .

# Définir la variable d'environnement pour éviter les problèmes d'encodage
ENV PYTHONUNBUFFERED=1

# Exposer le port sur lequel l'application Flask s'exécute
EXPOSE 5000

# Définir la commande pour exécuter l'application
CMD ["python", "app.py"]
