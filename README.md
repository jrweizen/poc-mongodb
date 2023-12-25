# poc-mongodb
-------------------


### DOCKER -----------------------------------------
docker build -t meu-mongodb-customizado .
docker run -d -p 27017:27017 --name meu-mongodb-container meu-mongodb-customizado
docker exec -it meu-mongodb-container /bin/sh  
docker stop $(docker ps -a -q) 
docker image rmi $(docker images ls) 

docker exec -it meu-mongodb-container mongod

### Mongod
https://www.howtogeek.com/devops/how-to-run-mongodb-in-a-docker-container/


### docker-compose.yaml ----------------------------
docker-compose up -d
docker exec -it python-app bash


### Mongo ------------
mongodb://localhost
docker exec -it mongodb bash    
docker exec -it mongodb mongosh 

show collections

db.tecnologiasdisruptivas.find()

db.createCollection("nomedacolecao")
db.nomedacolecao.insert({
    campo1: "valor1",
    campo2: "valor2",
    campo3: "valor3",
    campo4: "valor4"
})

db.getCollection("tecnologiasdisruptivas").getDB()