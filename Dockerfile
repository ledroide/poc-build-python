FROM python:alpine
# update
RUN apk add --update python3 py-pip
# install dependencies
RUN pip3 install -r requirements.txt
# bundle app
COPY /myproject /app

EXPOSE 8080
ENTRYPOINT ["python3", "/app/main.py"]