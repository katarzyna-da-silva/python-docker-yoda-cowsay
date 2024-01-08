# version normal

FROM python:3-alpine

WORKDIR . /cowsay

COPY . /app
COPY requirements.txt ./
RUN pip install -r requirements.txt \ apk --no-cache add python3
CMD ["sh", "cowsay.sh"]

# version min 

FROM python:3-slim

WORKDIR . /cowsay

COPY . /app
COPY requirements.txt ./
RUN pip install -r requirements.txt \ apk --no-cache add python3
CMD ["sh", "cowsay.sh"]