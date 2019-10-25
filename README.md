# ConsulOnDockerDemo
A project I've made a few years back - Consul running inside docker containers.

Note that this project was built in 2015, and both Docker and Consul made significant since then.

# Setup
how to setup consul on containers:

Start leader: 
```
docker run -d -p 8400:8400 -p 8500:8500 -p 8600:53/udp -h node1 progrium/consul -server -bootstrap -ui-dir /ui
```

Get node1's ip: ```docker ps``` -> copy the node1's id -> ```docker inspect id | grep 172```

Change the ip in httpd_consul's script file, client1.json to node1's ip

Rebuild httpd_consul image: 
```
docker build -t httpd_consul . (from the httpd_consul folder)
```

Start the Consul containers:
```
docker run -p 80:80 -p 8401:8400 -p 8501:8500 -p 8601:53/udp -h node2 httpd_consul
```

key location: /data/tmp/state<number>/data.mdb
