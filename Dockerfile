# ステージ1: Graphvizの抽出用 (変更なし)
FROM ubuntu:22.04 AS graphviz-provider
RUN apt-get update && apt-get install -y --no-install-recommends \
    graphviz \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

# ステージ2: メインイメージ
FROM docker.io/nvidia/cuda:13.0.0-devel-ubuntu22.04 

ENV DEBIAN_FRONTEND=noninteractive
ENV PYTHONUNBUFFERED=1

# Graphviz関連のコピー (変更なし)
COPY --from=graphviz-provider /usr/bin/dot /usr/bin/dot
COPY --from=graphviz-provider /usr/lib /usr/lib
COPY --from=graphviz-provider /usr/share/graphviz /usr/share/graphviz

# 追加: フォントおよびフォント設定ライブラリのインストール
RUN apt-get update && apt-get install -y --no-install-recommends \
    python3-pip \
    python3-dev \
    git \
    fontconfig \
    fonts-liberation \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

RUN pip install --no-cache-dir --upgrade pip
RUN pip install --no-cache-dir \
    numpy \
    matplotlib \
    cupy-cuda13x  \
    jupyterlab \
    graphviz

WORKDIR /app
COPY . /app/ 

# 追加: フォントキャッシュの更新
RUN fc-cache -fv

CMD ["/bin/bash"]
