docker network create service1-network

docker build -t service1 .
docker run -d --network service1-network --name service1 service1    

sudo docker run -d -p 80:80 --mount type=bind,source=$(pwd)/nginx.conf,target=/etc/nginx/nginx.conf --network service1-network --name service1-proxy nginx:alpine