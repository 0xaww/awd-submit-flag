FROM tutum/lamp


RUN sed -i "s/http:\/\/archive.ubuntu.com/http:\/\/mirrors.tuna.tsinghua.edu.cn/g" /etc/apt/sources.list
RUN apt-get update
RUN apt-get install -y lib32z1 socat


RUN useradd -m ctf

COPY ./html /var/www/html


WORKDIR /home/ctf

COPY ./start.sh /start.sh
RUN chmod +x /start.sh

COPY ./bin/ /home/ctf/
RUN chmod 740 /home/ctf/flag


CMD ["/start.sh"]
