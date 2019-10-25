FROM httpd_container

ENV container docker
VOLUME [ "/sys/fs/cgroup" ]
VOLUME [ "~/httpd_consul" ]

#consul part
COPY consul /root/consul
COPY client1.json /root/client1.json
COPY script /root/script
COPY script-httpd /root/script-httpd
COPY check_http.py /root/check_http.py
COPY httpd.conf /usr/local/apache2/htdocs/
COPY run-httpd.sh /root/run-httpd.sh
COPY var /var
COPY watch1.json /root/watch1.json
COPY my-key-handler.sh /usr/bin/my-key-handler.sh
COPY web.config /root/web.config
COPY images/consulvisio.PNG /var/www/html/consulvisio.PNG
COPY images/consulflow.PNG  /var/www/html/consulflow.PNG
COPY eventlog.txt /var/www/html/eventlog.txt

RUN adduser consul
RUN mkdir -p /etc/consul.d/{bootstrap,server,client}
RUN mkdir /var/consul
RUN chown consul:consul /var/consul
ENV web { "service": {"name": "webforconsul","tags": ["master"],"address": "127.0.0.1","port": 80,"checks": [{"script": "/root/check_http.py","interval": "10s"}]}}
RUN echo web > /etc/consul.d/client/config.json

#ports,permmisions
EXPOSE 80
EXPOSE 8300 8301 8301/udp 8302 8302/udp 8400 8500 53 53/udp 9301 10301 11301
RUN chmod 777 ./root/script
RUN chmod 777 ./root/script-httpd
RUN chmod 777 ./root/check_http.py
RUN chmod 777 /usr/local/apache2/htdocs/
RUN chmod 777 ./root/run-httpd.sh
RUN chmod 777 /root/watch1.json
RUN chmod 777 /usr/bin/my-key-handler.sh
RUN chmod 777 /root/web.config
RUN chmod 777 /var/www/html/index.html
RUN chmod 777 /var/www/html/consulvisio.PNG
RUN chmod 777 /var/www/html/consulflow.PNG
RUN chmod 777 /var/www/html/eventlog.txt

CMD "/root/script"

