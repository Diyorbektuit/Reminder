# _**Reminder Task Management System**_

Reminder — bu vazifalarni boshqarish tizimi bo‘lib, u Redis, Celery va Docker-dan foydalangan holda 
zamonaviy mikroxizmat arxitekturasini qo‘llab-quvvatlaydi.

## **📦 Loyiha tarkibi**

Loyiha quyidagi asosiy texnologiyalar va komponentlardan foydalanadi:

- Python: Asosiy backend logikasi uchun.
- Django: Web application yaratish va ma'lumotlar bazasi boshqaruvi uchun.
- Redis: Keshlash va vazifalarni navbatga qo'yish uchun.
- Celery: Asinxron fon vazifalarini boshqarish uchun.
- Docker: Muhitni izolyatsiya qilish va xizmatlarni boshqarish uchun.
- PostgreSQL: Ma'lumotlar bazasi uchun.
- python-telegram-bot: telegram bot uchun 
- SqlAlchemy: Telegram bot state management uchun

## **🚀 O'rnatish va ishga tushirish**

Quyidagi bosqichlar orqali loyihani mahalliy mashinangizda ishga tushiring:

### **1. Muhitni sozlash**

Loyiha uchun talab qilinadigan barcha paketlarni o'rnatish uchun virtual muhit yarating va faollashtiring:
```bash
python -m venv .venv
source .venv/bin/activate   # Windows uchun: .venv\Scripts\activate
pip install -r requirements.txt
```

### **2. Docker Compose-ni ishga tushirish**

Docker konteynerlarini ishga tushiring:
```bash
docker-compose up --build
```

### **3. Migratsiyalarni qo'llash**

Django migratsiyalarini ishlatib, ma'lumotlar bazasini sozlang:
```bash
docker-compose exec web python manage.py migrate
```

### **4. Superuser yaratish**

Admin panelga kirish uchun superuser yarating:
```bash
docker-compose exec web python manage.py createsuperuser
```

### **5. Loyihani ishga tushirish**

Mahalliy serverni ishga tushiring:
```bash
docker-compose up
```
Mahalliy serveringiz quyidagi URL manzilida ishga tushadi: http://localhost:8000

## **🔑 Muhim sozlamalar**

Loyiha .env faylidan foydalanadi. Quyida .env.example faylidan foydalanib o'z .env faylingizni yarating

## **⚙️ Texnologik stack**

- Backend: Django, Celery, Redis, SqlAlchemy
- Ma'lumotlar bazasi: PostgreSQL, sqlite
- Muhit boshqaruvi: Docker va Docker Compose

