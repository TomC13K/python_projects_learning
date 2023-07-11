FROM python:3.10-slim
RUN mkdir -p /app
WORKDIR /app
COPY requirements.txt .
COPY main.py .
COPY ./app /app/app
RUN pip3 install --no-cache-dir -r requirements.txt
EXPOSE 8000
CMD ["python3", "main.py"]
