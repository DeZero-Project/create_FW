FROM docker.io/nvidia/cuda:13.0.0-devel-ubuntu22.04
# 環境変数の設定
ENV DEBIAN_FRONTEND=noninteractive
ENV PYTHONUNBUFFERED=1

RUN apt-get update && apt-get install -y --no-install-recommends \
    python3-pip \
    python3-dev \
    git \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

RUN pip install --no-cache-dir --upgrade pip

# cupy-cudaXXX は、ベースイメージのCUDAメジャーバージョンに合わせて選択
RUN pip install --no-cache-dir \
    numpy \
    matplotlib \
    cupy-cuda13x \
    jupyterlab

WORKDIR /app
COPY . /app/

CMD ["/bin/bash"]