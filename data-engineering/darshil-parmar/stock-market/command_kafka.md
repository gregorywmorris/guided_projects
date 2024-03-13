# Kafka EC2 Set up

## 1 Create Instance

1. Edit security to allow all traffic from your local IP only

## 2 Install and Configure Kaka

1. SSH into instance
1. Install Kafka
    -`wget https://downloads.apache.org/kafka/3.7.0/kafka_2.12-3.7.0.tgz`
    - `tar -xvf kafka_2.12-3.7.0.tgz`
1. Install java
    - `curl -O https://download.java.net/java/GA/jdk11/13/GPL/openjdk-11.0.1_linux-x64_bin.tar.gz`
    - `tar zxvf openjdk-11.0.1_linux-x64_bin.tar.gz`
    - `mv jdk-11.0.1 /usr/local/`
    - `vi /etc/profile.d/jdk11.sh`

        ```bash
        # create new
        export JAVA_HOME=/usr/local/jdk-11.0.1
        export PATH=$PATH:$JAVA_HOME/bin
        export KAFKA_HEAP_OPTS="-Xmx256M -Xms128M"
        ```

    - See top answer here for [heap explanation](https://stackoverflow.com/questions/21448907/kafka-8-and-memory-there-is-insufficient-memory-for-the-java-runtime-environme)
    - `source /etc/profile.d/jdk11.sh`
    - `java --version`

        ```text
        openjdk 11.0.1 2018-10-16
        OpenJDK Runtime Environment 18.9 (build 11.0.1+13)
        OpenJDK 64-Bit Server VM 18.9 (build 11.0.1+13, mixed mode)
        ```

1. kafka is pointing to private server IP, change server.properties so that it can run in public IP. Update advertized.listeners to be active with current host name.
1. `sudo vi kafka_2.12-3.7.0/config/server.properties`

    ```bash
    advertised.listeners=PLAINTEXT:your-host-name:9092
    ```

## 3 Start Zoo-keeper

1. SSh into instance in a new window
1. `kafka_2.12-3.7.0/bin/zookeeper-server-start.sh kafka_2.12-3.7.0/config/zookeeper.properties`

## 4 Start Kafka-server

1. SSh into instance in a new window
1. `kafka_2.12-3.7.0/bin/kafka-server-start.sh kafka_2.12-3.7.0/config/server.properties`

## 5 Create the topic

1. SSh into instance in a new window
1. `kafka_2.12-3.7.0/bin/kafka-topics.sh --create --topic demo_testing --bootstrap-server {Put the Public IP of your EC2 Instance:9092} --replication-factor 1 --partitions 1`

## 6 Start Producer

1. `kafka_2.12-3.7.0/bin/kafka-console-producer.sh --topic demo_testing --bootstrap-server {Put the Public IP of your EC2 Instance:9092}`

## 7 Start Consumer

1. SSh into instance in a new window
1. `kafka_2.12-3.7.0/bin/kafka-console-consumer.sh --topic demo_testing --bootstrap-server {Put the Public IP of your EC2 Instance:9092}`
