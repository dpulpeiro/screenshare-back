FROM python:3.9-alpine3.17

COPY devops/prod/requirements.txt /app/requirements.txt

RUN pip install --no-cache-dir -r /app/requirements.txt

COPY src /app

WORKDIR /app

ENTRYPOINT ["python","main.py"]
