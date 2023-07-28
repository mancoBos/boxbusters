FROM python:3.9.16-slim-buster

RUN adduser --system --no-create-home nonroot &&\
    mkdir -p /app
COPY . app.py /app/
COPY src /app/
WORKDIR /app
RUN pip install --no-cache-dir -r requirements.txt
USER nonroot
EXPOSE 8080/tcp

CMD [ "python", "./main.py" ]