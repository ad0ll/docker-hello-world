FROM python:alpine

WORKDIR /app/

COPY . .

RUN pip install -Ur requirements.txt

CMD ["python", "main.py"]