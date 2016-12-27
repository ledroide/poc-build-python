FROM python:2-onbuild
COPY main.py /app
EXPOSE 8080 
ENTRYPOINT ["python", "/app/main.py"]