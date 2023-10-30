FROM python:3.12.0-alpine

WORKDIR /app

# 將依賴文件複製到工作目錄
COPY requirements.txt /app/

RUN pip install --no-cache-dir -r requirements.txt

COPY app/ /app/

EXPOSE 5000

CMD ["python", "app.py"]
