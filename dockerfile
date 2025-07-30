# Dockerfile

# 1. Mulai dari gambar dasar Python
FROM python:3.12-slim

# 2. Atur direktori kerja di dalam kontainer
WORKDIR /app

# 3. Salin semua file proyek Anda ke dalam kontainer
COPY . .

# 4. Instal semua library dari requirements.txt
RUN pip install --no-cache-dir -r requirements.txt