# コンテナ起動用スクリプト

# 目的のコンテナIDまたはイメージ名
IMAGE_NAME="fw"

# 手動でデバイスとライブラリパスをマウント
podman run -it --rm \
    --privileged \
    --security-opt label=disable \
    --device /dev/nvidia-modeset:/dev/nvidia-modeset \
    --device /dev/nvidia-uvm:/dev/nvidia-uvm \
    --device /dev/nvidiactl:/dev/nvidiactl \
    --device /dev/nvidia0:/dev/nvidia0 \
    --gpus all \
    -v "$(pwd)":/app:Z \
    -v /usr/lib/x86_64-linux-gnu:/usr/lib/x86_64-linux-gnu:ro \
    "$IMAGE_NAME" \
    /bin/bash -c "ldconfig && exec /bin/bash"