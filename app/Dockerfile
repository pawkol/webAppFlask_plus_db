# Użycie obrazu Python jako bazowego
FROM python:3.9-slim

# Ustawienie katalogu roboczego
WORKDIR /app

# Skopiowanie plików aplikacji do kontenera
COPY . /app

# Instalacja zależności
RUN pip install Flask mysql-connector-python

# Uruchomienie aplikacji
CMD ["python", "app.py"]

