FROM python:3.8-alpine

ARG PUID=1000
ARG PGID=1000
ARG TOKEN=needed
ARG HOSTNAME=birdbot
ENV PUID=$PUID
ENV PGID=$PGID
ENV TOKEN=$TOKEN
ENV HOSTNAME=$HOSTNAME

# Installing Kubectl with the binary
RUN apk add sudo && apk add curl
RUN curl -LO https://dl.k8s.io/release/v1.24.6/bin/linux/amd64/kubectl
RUN sudo install -o root -g root -m 0755 kubectl /usr/local/bin/kubectl
RUN apk del sudo curl

# Add bot user
RUN adduser --disabled-password --shell /bin/bash botman
ENV LANG en_US.utf8

# home directory
WORKDIR /home/botman

# Adding the actual python script and the requirements we need
ADD birdbot.py /home/botman
COPY requirements.txt /home/botman

# apply permissions
RUN chown -R $PUID:$PGID /home/botman

# switch to user and installing the discord modules under that user
USER botman
RUN pip install -r requirements.txt

CMD ["python","-u","/home/botman/birdbot.py"]
