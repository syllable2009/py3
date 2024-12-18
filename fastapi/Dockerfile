# 使用官方的 Python 运行时作为基础镜像
#FROM python:3.9-slim
FROM python:3.9-slim-playwright

# 设置工作目录
WORKDIR /app

# 复制 requirements.txt 并安装依赖
COPY app/requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# 复制整个应用程序代码
COPY app ./app

# 暴露 FastAPI 默认端口
EXPOSE 8000

# docker build -t fast:1.2 .
# docker run -d --name fast2 -p 8082:8000 --restart unless-stopped fast:1.2
# 运行 FastAPI 应用后访问http://localhost:8000/redoc或http://localhost:8000/docs
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]