Build and run containers:

    docker-compose up --build

Connect to the running web_app container:

    docker exec -it docker_web_app_1 bash

Then you can install ping and check the connectivity from one container to another:

    apt update
    apt install iputils-ping
    ping db
        
Also you can install postgres client and check connectivity to a db:
    
    apt update    
    apt install postgresql-client-13
    psql -h db -p 5432 -d hello_flask_dev -U hello_flask
    # password is in the docker-compose
    
You can connect to postgres container from a host machine.
Find the IP address of the postgres container 
    
    docker inspect -f '{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' docker_db_1

then you can connect to it using postgres client:
    
    psql -h 172.18.0.2 -p 5432 -d hello_flask_dev -U hello_flask