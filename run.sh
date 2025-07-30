xhost +

docker run -it --gpus all \
  -v $(pwd):/workspace \
  -w /workspace trajopt bash

