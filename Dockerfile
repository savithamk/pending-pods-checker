FROM python:3.8

RUN pip install kubernetes

COPY pod-checker.py /app/pod-checker.py

CMD ["python", "/app/pod-checker.py"]
