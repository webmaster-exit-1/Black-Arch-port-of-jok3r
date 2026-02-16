FROM archlinux:latest
LABEL maintainer="xst3nz@gmail.com"
LABEL maintainer="pentux@protonmail.com"

# NOTE: This Dockerfile is used to rebuild Jok3r Docker Image from scratch
# It is recommended to directly pull koutto/jok3r image from Docker Hub instead

LABEL org.label-schema.name="koutto/jok3r"
LABEL org.label-schema.description="Docker Image for Jok3r - Network and Web Pentest Automation Framework"
LABEL org.label-schema.usage="https://github.com/koutto/jok3r"
LABEL org.label-schema.url="https://www.jok3r-framework.com"
LABEL org.label-schema.docker.cmd="docker run -i -t -w /root/jok3r -e DISPLAY=$DISPLAY -v /tmp/.X11-unix:/tmp/.X11-unix --shm-size 2g --net=host koutto/jok3r"

# Initialize BlackArch repository
RUN curl -O https://blackarch.org/strap.sh && \
    chmod +x strap.sh && \
    ./strap.sh && \
    rm -f strap.sh && \
    pacman -Syu --noconfirm

# Install Jok3r dependencies via pacman
RUN pacman -S --noconfirm \
    python python-pip \
    rbenv ruby-build \
    git wget curl gawk sudo procps-ng \
    gcc make pkg-config \
    && pacman -Scc --noconfirm

WORKDIR /root

# Initialize rbenv for Ruby tools
RUN echo 'export PATH="$HOME/.rbenv/bin:$PATH"' >> /root/.bashrc && \
    echo 'eval "$(rbenv init -)"' >> /root/.bashrc && \
    echo 'export LC_ALL="en_US.UTF-8"' >> /root/.bashrc && \
    echo 'export LANG="en_US.UTF-8"' >> /root/.bashrc && \
    echo 'export LANGUAGE="en_US:en"' >> /root/.bashrc && \
    echo 'export PS1="\[$(tput bold)\]\[$(tput setaf 2)\]\u@jok3r-docker:\[$(tput setaf 4)\]\w\\$\[$(tput sgr0)\]\[$(tput sgr0)\] "' >> /root/.bashrc && \
    echo "gem: --no-rdoc --no-ri" >> /root/.gemrc && \
    echo 'jok3r() { python3 ~/jok3r/jok3r.py "$@"; }' >> /root/.bashrc && \
    git clone https://github.com/koutto/jok3r.git

# Set the locale
ENV LANG en_US.UTF-8
ENV LANGUAGE en_US:en
ENV LC_ALL en_US.UTF-8
ENV PYTHONIOENCODING utf-8

WORKDIR /root/jok3r

RUN ./install-all.sh
