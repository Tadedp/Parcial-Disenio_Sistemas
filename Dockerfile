FROM python:3.9-slim

WORKDIR /app

COPY /app /app/

RUN pip install --no-cache-dir --user -r requirements.txt

EXPOSE 8000

ENV PYTHONUNBUFFERED=1

CMD ["python", "main.py"]