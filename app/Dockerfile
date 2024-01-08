FROM python:3.10-slim

WORKDIR /app

COPY app/tux.py .

RUN apt-get update && \
    apt-get install -y --no-install-recommends lolcat && \
    apt-get install -y --no-install-recommends bsdmainutils && \ 
    rm -rf /var/lib/apt/lists/*

# Set the entrypoint
ENTRYPOINT ["python", "tux.py"]