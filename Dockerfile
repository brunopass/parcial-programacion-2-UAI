FROM python:3.8-slim-buster as develop
WORKDIR /app
COPY . .
CMD ["python3", "__main__.py"]