FROM python:alpine
RUN apk add --no-cache openssl

RUN openssl req -x509 -newkey rsa:4096 -keyout key.pem -out cert.pem -days 365 -subj "/C=AL/ST=Tirana/L=Tirana/O=TRGProject/OU=TRG/CN=localhost" -nodes

RUN mkdir -p /etc/ssl_certs
RUN cp cert.pem /etc/ssl_certs/cert.pem && \
    cp key.pem /etc/ssl_certs/key.pem

WORKDIR /code
COPY dependencies.txt .
RUN pip install -r dependencies.txt
COPY src/ .
CMD [ "python", "./hello_world.py"]
EXPOSE 8087
