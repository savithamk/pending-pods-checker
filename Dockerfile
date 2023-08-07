FROM python:3.11.1-alpine

ENV PYTHONUNBUFFERED 1

RUN pip install kubernetes

COPY pod-checker.py /app/pod-checker.py

CMD ["python", "/app/pod-checker.py"]
