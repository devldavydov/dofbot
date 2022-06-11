FROM ubuntu:22.04

RUN apt update && \
    apt install -y python3 python3-pip && \
    mkdir -p /tmp/dofbot

WORKDIR /tmp/dofbot

COPY source ./source
COPY pyproject.toml .
COPY setup.py .

RUN pip install .

ENTRYPOINT ["dofbot"]
