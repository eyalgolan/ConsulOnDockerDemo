# ConsulOnDockerDemo
A project I've made a few years back - Consul running inside docker containers

# Setup
how to setup consul on containers:
a. start leader: docker run -d -p 8400:8400 -p 8500:8500 -p 8600:53/udp -h node1 progrium/consul -server -bootstrap -ui-dir /ui
b. get node1's ip: docker ps -> copy the node1's id -> docker inspect id | grep 172
c. change the ip in httpd_consul's script file, client1.json to node1's ip
d. rebuild httpd_consul image: docker build -t httpd_consul . (from the httpd_consul folder)
e. docker run -p 80:80 -p 8401:8400 -p 8501:8500 -p 8601:53/udp -h node2 httpd_consul

key location: /data/tmp/state<number>/data.mdb
