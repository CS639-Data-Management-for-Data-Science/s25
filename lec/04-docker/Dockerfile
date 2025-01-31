FROM ubuntu:24.04
RUN apt-get update
RUN apt-get install -y unzip python3 python3-pip
RUN pip3 install pandas --break-system-packages

COPY hello.py /var/run/hello.py
CMD ["python3", "/var/run/hello.py"]
