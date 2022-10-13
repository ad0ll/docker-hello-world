FROM python:alpine

WORKDIR /app/

COPY requirements.txt .
RUN pip install -Ur requirements.txt
COPY . .

CMD ["python", "main.py"]