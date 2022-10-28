FROM openjdk:8-alpine
# Download Spark 
RUN wget https://dlcdn.apache.org/spark/spark-3.3.1/spark-3.3.1-bin-hadoop3.tgz
# Install and extract Spark
RUN tar -xzf spark-3.3.1-bin-hadoop3.tgz && \
    mv spark-3.3.1-bin-hadoop3 /spark && \
    rm spark-3.3.1-bin-hadoop3.tgz