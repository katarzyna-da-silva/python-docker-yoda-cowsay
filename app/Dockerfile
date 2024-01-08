# version normal

FROM python:3-alpine

WORKDIR . /cowsay

COPY . /app
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
RUN apk --no-cache add python
CMD ["sh", "cowsay.sh"]

# version min 

FROM python:3-slim

WORKDIR . /cowsay

COPY . /app
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
RUN apk --no-cache add python
CMD ["sh", "cowsay.sh"]