FROM python:3.10-slim

WORKDIR /app

# Requirements fayllarini konteynerga nusxalash
COPY ./requirements/develop.txt /app/requirements/develop.txt
COPY ./requirements/base.txt /app/requirements/base.txt
COPY ./requirements/production.txt /app/requirements/production.txt

# wait-for-it.sh skriptini nusxalash
COPY wait-for-it.sh /app/wait-for-it.sh
RUN chmod +x /app/wait-for-it.sh  # Skriptni ishga tushirish huquqini berish

# Python paketlarini o'rnatish
RUN pip install --upgrade pip
RUN pip install -r /app/requirements/production.txt
RUN pip install gunicorn
RUN apt-get update && apt-get install -y redis-tools

# App fayllarini nusxalash
COPY . .

# Portni ochish
EXPOSE 8000

# To'g'ri komanda
ENTRYPOINT ["/app/wait-for-it.sh", "db:5432", "--"]

# Asl komanda: serverni ishga tushirish
CMD ["python", "manage.py", "runserver", "0.0.0.0:8004"]

# Docker uchun umumiy fayllarga ruxsat berish
RUN chmod a+x /app/*
