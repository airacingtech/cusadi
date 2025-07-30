FROM nvidia/cuda:12.3.2-devel-ubuntu22.04

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && apt-get install -y \
    build-essential \
    cmake \
    git \
    wget \
    curl \
    python3.10 \
    python3.10-dev \
    python3-pip \
    python3-venv \
    gcc-12 g++-12 \
    && rm -rf /var/lib/apt/lists/*

RUN ln -sf /usr/bin/python3.10 /usr/bin/python && \
    ln -sf /usr/bin/pip3 /usr/bin/pip

RUN pip install --upgrade pip && \
    pip install casadi==3.6.5 numpy torch

ENV CC=/usr/bin/gcc-12
ENV CXX=/usr/bin/g++-12
ENV CMAKE_CUDA_HOST_COMPILER=/usr/bin/g++-12

WORKDIR /workspace

