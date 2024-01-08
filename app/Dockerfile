FROM python:3.10

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

RUN apt-get update \
    && apt-get install -y bsdmainutils cowsay toilet lolcat

RUN apt-get update && \
    apt-get install -y --no-install-recommends lolcat && \
    apt-get install -y --no-install-recommends bsdmainutils && \ 
    rm -rf /var/lib/apt/lists/*

ENTRYPOINT ["/app/cowsay.sh"]