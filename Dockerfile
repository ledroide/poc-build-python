FROM python:2-alpine
COPY /myproject /app
EXPOSE 8080
ENTRYPOINT ["python", "/app/main.py"]