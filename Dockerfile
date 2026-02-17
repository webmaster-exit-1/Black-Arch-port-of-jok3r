FROM archlinux:latest
LABEL maintainer="xst3nz@gmail.com"

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

# Install Jok3r dependencies
RUN pacman -S --noconfirm python python-pip rbenv ruby-build git

# Initialize rbenv for Ruby tools
RUN echo 'export PATH="$HOME/.rbenv/bin:$PATH"' >> ~/.bashrc && \
    echo 'eval "$(rbenv init -)"' >> ~/.bashrc

WORKDIR /root/jok3r

RUN python3 update.py