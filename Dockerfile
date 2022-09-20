FROM apache/airflow:2.3.4-python3.8

USER root

RUN apt-get update -y && \
    apt-get upgrade -yqq && \
    apt install openjdk-11-jdk -yqq && \
    apt-get install -y --no-install-recommends \
    vim \
    curl \
    wget \
    git && \
    apt-get autoremove -yqq --purge && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists


ENV JAVA_HOME=/usr/lib/jvm/java-1.11.0-openjdk-amd64

USER airflow

COPY ./requirements.txt .

RUN pip install --upgrade pip && \
    pip install -r requirements.txt

