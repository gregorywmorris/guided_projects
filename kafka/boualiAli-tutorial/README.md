# Kafka Tutorial

#### Conduktor Git

Full stack
To ease you journey with kafka just connect to localhost:8080

login: admin@admin.io password: admin

Conduktor-platform: $DOCKER_HOST_IP:8080
Single Zookeeper: $DOCKER_HOST_IP:2181
Single Kafka: $DOCKER_HOST_IP:9092
Kafka Schema Registry: $DOCKER_HOST_IP:8081
Kafka Rest Proxy: $DOCKER_HOST_IP:8082
Kafka Connect: $DOCKER_HOST_IP:8083
KSQL Server: $DOCKER_HOST_IP:8088
(experimental) JMX port at $DOCKER_HOST_IP:9001
Run with:

docker compose -f full-stack.yml up
docker compose -f full-stack.yml down
** Note: if you find that you can not connect to localhost:8080 please run docker compose -f full-stack.yml build to rebuild the port mappings