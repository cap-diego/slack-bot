docker run -it --name rabbitmq -p 5672:5672 -p 15672:15672 rabbitmq
#docker run -d --hostname my-rabbit --name some-rabbit rabbitmq:3
#docker run \
#    -it \
#    --name rabbitmq \
#    -p 5672:5672 \
#    -p 15672:15672 \
#    -e RABBITMQ_DEFAULT_USER=diego \
#    -e RABBITMQ_DEFAULT_PASS=prueba1 \
#    -v /docker-data/rabbitmq/data:/var/lib/rabbitmq \
#    -d rabbitmq:management \
#    --host-name my-rabbit \
