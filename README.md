# Containerized Web Service with Load Balancer

## Objective

A web service that runs behind a load balancer using Docker containers. The web service sends back a message based on a configuration file, and you can start everything with just one command.


## Prerequisites
- Docker
- Docker Compose 

## Architecture
There are 2 application, loadbalancer which is an nginx server and webserver, which is a flask application. 
Loadbalancer redirects all the traffic to the webserver. Used network address translation in nginx.conf for redirecting to the webserver container. 


## Run
Run the whole applicaiton by running just 1 cmd
```bash
docker compose up
```
 Access application through `http://localhost:80`

