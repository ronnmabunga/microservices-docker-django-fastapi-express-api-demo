# Django Dockerfile
FROM python:3.10-slim

ENV PYTHONUNBUFFERED 1
WORKDIR /app

COPY django-main/requirements.txt .
RUN pip install -r requirements.txt

COPY django-main /app

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
