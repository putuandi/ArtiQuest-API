FROM python:3.10.12-slim

WORKDIR /app

COPY . ./app

RUN pip install -r requirements.txt

CMD exec gunicorn --bind :$PORT --workers 1 --threads 8 --timeout 0 main:app

# FROM python:3.10-bullseye

# WORKDIR /app
# COPY . .
# RUN pip install -r requirement.txt
# EXPOSE 8000
# CMD ["uvicorn", "main:app", "--reload"]