#stage 1 : build stage
FROM python:3.8-slim AS build-stage

WORKDIR /app

RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc \
    python3-dev \
    default-libmysqlclient-dev \
    pkg-config && rm -rf /var/lib/apt/lists/*

    COPY . .

    RUN pip install flask mysqlclient

    #stage 2 production stage
FROM python:3.8-slim 

WORKDIR /app

COPY --from=build-stage /app /app

EXPOSE 5002

CMD ["python", "app.py"]