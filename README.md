# spacy_docker_gpu
Minimal project to test Spacy with GPU using Docker


Create Docker Image

`docker build -t cupy_api .`

Run Docker Container

`docker run --gpus all -p 5501:5501 cupy_api`