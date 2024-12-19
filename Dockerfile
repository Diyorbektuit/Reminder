FROM python:3.10-slim

WORKDIR /app

COPY . /app/

RUN pip install --no-cache-dir -r requirements/develop.txt

CMD ["python", "manage.py", "runserver", "0.0.0.0:8004"]
