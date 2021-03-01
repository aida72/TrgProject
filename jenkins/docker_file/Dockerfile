FROM jenkins/jenkins:alpine

ENV CRYPTOGRAPHY_DONT_BUILD_RUST=1
COPY plugins.txt /usr/share/jenkins/plugins.txt
RUN /usr/local/bin/install-plugins.sh < /usr/share/jenkins/plugins.txt
USER root
RUN apk add --no-cache \
	bc \
    docker \
    py3-pip \
    python3-dev \
    libffi-dev \
    musl-dev \ 
    openssl-dev \ 
    gcc \ 
    libc-dev \ 
    make \
    curl \
	logrotate \
	nano \
	openssh \
    sudo \
    ansible \
	openrc

RUN apk add --no-cache openssl
RUN pip install docker-compose

RUN openssl genrsa -des3 -passout pass:aida -out server.pass.key 2048 && \
    openssl rsa -passin pass:aida -in server.pass.key -out jenkins.key && \
    rm server.pass.key && \
    openssl req -new -key jenkins.key -out jenkins.csr \
        -subj "/C=AL/ST=Tirana/L=Tirana/O=OrgName/OU=TRG/CN=localhost" && \
    openssl x509 -req -days 365 -in jenkins.csr -signkey jenkins.key -out jenkins.pem
    
RUN mkdir -p /var/lib/jenkins

RUN cp jenkins.pem /var/lib/jenkins/cert && \
    cp jenkins.key /var/lib/jenkins/pk && \
    chown jenkins:jenkins /var/lib/jenkins/cert && \
    chown jenkins:jenkins /var/lib/jenkins/pk

RUN apk add --no-cache python3

RUN pip install docker
RUN ansible-galaxy collection install community.docker

USER jenkins
ENV JENKINS_OPTS --httpPort=-1 --httpsPort=8088 --httpsCertificate=/var/lib/jenkins/cert --httpsPrivateKey=/var/lib/jenkins/pk
EXPOSE 8088

