# FastAPI Dockerfile
FROM python:3.10-slim

WORKDIR /app

COPY fastapi-task-service/requirements.txt .
RUN pip install -r requirements.txt

COPY fastapi-task-service /app

EXPOSE 8001

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8001"]
