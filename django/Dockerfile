# django dockerfile
FROM python:3.12-alpine
WORKDIR /app
COPY requirements.txt requirements.txt
RUN apk add --no-cache bash
RUN pip install -r /app/requirements.txt
COPY . .
COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

EXPOSE 5000
ENTRYPOINT ["/entrypoint.sh"]
