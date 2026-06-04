## Docker commands

- `docker`
- `docker pull --help`
- `cat /etc/os-release` # 24.04 LTS (Long Term Support)
- `docker pull ubuntu:26.04`
- `docker images`
- `docker tag ubuntu:26.04 myubuntu`
- `docker run ubuntu:26.04`
- `docker run ubuntu:26.04 echo hello`
- `docker run ubuntu:26.04 bash` # by default no stdin

### docker container
- `docker run -it ubuntu:26.04 bash` # by default no stdin
- `cat /etc/os-release`
- `echo $HOME` # default is root permission
- `rm -rf /*`
- `ls` # Ctrl + D
- `docker run ubuntu:25.04` # automatically pull
- `docker run ubuntuabc:25.04` # automatically pull

### docker container and image cleanup
- `docker ps` # active containers
- `docker ps -a` # active containers
- `docker rm <name>`
- `docker rm <container ID>`
- `docker ps -aq`
- `docker rm `docker ps -aq`` # second command in back ticks
- `docker ps -a`
- `docker rmi ubuntu:25.04`

## docker system commands
- `docker system`
- `docker system df`
- `docker system prune`

## container in background
- `docker run ubuntu sh -c "echo before && sleep 3 && echo after"`
- `docker run -d ubuntu sh -c "echo before && sleep 3000 && echo after"`
- `docker ps`
- `docker logs <name>`
- `docker logs -f <name>`
- `docker exec -it <name> bash`
- `ls`
- `ps ax`
- `kill <PID>` # if necessary
- `docker stats`
- `docker stop <name>` # gracefull
- `docker kill <name>` # stronger kill signal
- `docker rm <name>`

## Dockerfile

```
FROM # base image
RUN # something during docker build like package installation
COPY # file
CMD # default command
```

```
vim Dockerfile
FROM ubuntu
RUN apt-get update
RUN apt-get install unzip
```
- `docker build . -t demo`
- `docker images`
```
vim Dockerfile
FROM ubuntu
RUN apt-get update
RUN apt-get install unzip python3 python3-pip
```
- `docker build . -t demo` # cached layers and failure reason
```
vim Dockerfile
FROM ubuntu
RUN apt-get update && \
    apt-get install -y unzip python3 python3-pip
```
- `docker build . -t demo`
- `docker run -it demo bash`
- `python3`
- ``pip3 install pandas==2.3.3`
- `pip3 install pandas==2.3.3 --break-system packages`

```
vim Dockerfile
FROM ubuntu
RUN apt-get update && \
    apt-get install -y unzip python3 python3-pip
RUN pip3 install pandas==2.3.3 --break-system packages
```
```
vim myapp.py
import pandas as pd
mySeries = pd.Series([1,2,3])
print(mySeries.sum())
```
- `python3 myapp.py`
```
vim Dockerfile
FROM ubuntu
RUN apt-get update && \
    apt-get install -y unzip python3 python3-pip
RUN pip3 install pandas==2.3.3 --break-system packages
COPY ./myapp.py /myapp.py
CMD ["python3", "/myapp.py"]
```

- `docker build . -t demo`
- `docker run demo`
