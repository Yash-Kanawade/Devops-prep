FROM python:3.11-slim

WORKDIR /app

COPY app.py .

RUN useradd -m -u 1000 appuser && chown -R appuser:appuser /app

USER appuser

CMD ["python","app.py"]


