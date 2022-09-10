FROM python:3.10-slim
LABEL maintainer="Razevedo"

# Defining useful environment variables
ENV SPARK_VERSION=3.3.0
ENV HADOOP_VERSION=2.7
ENV SPARK_HOME=/usr/local/spark
ENV PYTHONHASHSEED=1
ENV SPARK_EXECUTOR_MEMORY=650m
ENV SPARK_DRIVER_MEMORY=650m
ENV SPARK_WORKER_MEMORY=650m
ENV SPARK_DAEMON_MEMORY=650m
ENV PATH $SPARK_HOME/bin/:$PATH

# Upgrade and install some tools and dependencies
RUN apt-get update -yqq && \
    apt-get upgrade -yqq && \
    apt-get install -yqq \
    netcat \
    apt-utils \
    curl \
    vim \
    ssh \
    net-tools \
    ca-certificates \
    jq \
    wget \
    software-properties-common

# Adding dependencies for PySpark
RUN pip install pyspark==${SPARK_VERSION}

# Installing Spark
WORKDIR ${SPARK_HOME}

COPY ./spark-3.3.0-bin-hadoop2.tgz .

RUN tar zxf spark-3.3.0-bin-hadoop2.tgz && \
    mv spark-3.3.0-bin-hadoop2/* . && \
    rm -rf spark-3.3.0-bin-hadoop2.tgz && \
    rm -rf spark-3.3.0-bin-hadoop2


RUN apt-get autoremove -yqq --purge && \
    apt-get clean && \
    rm -rf /tmp/* /var/tmp/*

RUN apt install default-jre -yqq

ENV JAVA_HOME=/usr/lib/jvm/java-1.11.0-openjdk-amd64

WORKDIR /

COPY ./entrypoint.sh .

RUN chmod +x entrypoint.sh

ENTRYPOINT [ "./entrypoint.sh" ]